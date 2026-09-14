"""V2 all-question AppTest audit; synchronous acknowledgments are modeled.
The separate shipped async regression suite exercises delayed events.
"""
import sys, json, time, logging
from pathlib import Path
from copy import deepcopy
from collections import Counter

HERE = Path(__file__).resolve().parent
HARNESS = HERE.parent
GENERATED = HERE / 'generated'
GENERATED.mkdir(exist_ok=True)
sys.path.insert(0, str(HARNESS))
assert (HARNESS / 'docs/question-bank.md').is_file(), 'Packaged study guide is required'
import streamlit
from streamlit.testing.v1 import AppTest
import browser_storage, collection_storage
from quiz_core import load_bank, validate_bank, is_correct, response_error, summarize
from progress_store import empty_progress, record_answer, restore_progress, restart_attempt

for name in ['streamlit.runtime.scriptrunner_utils.script_run_context', 'streamlit.runtime.state.session_state_proxy']:
    logging.getLogger(name).setLevel(logging.ERROR)
STORE = {}
WRITES = Counter()

def sync(payload, *, bank_id=browser_storage.DEFAULT_BANK_ID, replacement_id=None, expected_baseline=None):
    if payload is None:
        return {'status': 'loaded', 'payload': deepcopy(STORE.get(bank_id)), 'baseline_id': 'modeled-baseline'}
    STORE[bank_id] = deepcopy(payload)
    WRITES[bank_id] += 1
    return {'status': 'saved', 'request_id': browser_storage.storage_request_id(payload, replacement_id=replacement_id), 'baseline_id': 'modeled-baseline'}

def snapshot(token):
    return {'status': 'loaded', 'records': {b: deepcopy(STORE.get(b)) for b in collection_storage.BANK_IDS}, 'errors': {}}

browser_storage.sync_storage = sync
collection_storage.read_collection_progress = snapshot

LEDGER = {'streamlit_version': streamlit.__version__, 'coverage': {}, 'sets': [], 'findings': [], 'started_at': time.strftime('%Y-%m-%dT%H:%M:%S%z')}
COUNT = Counter()
START = time.monotonic()

def save():
    LEDGER['coverage'] = dict(COUNT)
    LEDGER['elapsed_seconds'] = round(time.monotonic() - START, 2)
    (GENERATED / 'functional-results.json').write_text(json.dumps(LEDGER, indent=2))

def check(at):
    assert not at.exception, [(e.message, e.stack_trace) for e in at.exception]

def start(n):
    at = AppTest.from_file(HARNESS / 'app.py', default_timeout=30)
    at.query_params['set'] = str(n)
    at.run()
    check(at)
    return at

def run(at):
    at.run()
    COUNT['apptest_script_runs'] += 1
    check(at)

def click(at, label):
    button = next(b for b in at.button if b.label == label)
    assert not button.disabled, label
    button.click()
    run(at)

def jump(at, q, review=False):
    at.selectbox(key='review_question' if review else 'jump').set_value(q['id'])
    run(at)

def answer(q):
    return {p['id']: p['answer'] for p in q['pairs']} if q['type'] == 'matching' else deepcopy(q['answer'])

def wrong(q):
    response = answer(q)
    if q['type'] == 'matching':
        k = next(iter(response))
        response[k] = next(c['id'] for c in q['choices'] if c['id'] != response[k])
    else:
        response[0] = next(c['id'] for c in q['choices'] if c['id'] not in response)
        response = [c['id'] for c in q['choices'] if c['id'] in response]
    return response

def set_response(at, q, response, review=False):
    prefix = 'review_' if review else ''
    qid = q['id']
    if q['type'] == 'single':
        at.radio(key=f'{prefix}single_{qid}').set_value(response[0])
    elif q['type'] == 'multiple':
        for c in q['choices']:
            at.checkbox(key=f'{prefix}multi_{qid}_{c["id"]}').set_value(c['id'] in response)
    else:
        for p in q['pairs']:
            at.selectbox(key=f'{prefix}match_{qid}_{p["id"]}').set_value(response[p['id']])

def check_reveal(at, q):
    text = '\n'.join(m.value for m in at.markdown)
    assert q['prompt'] in text, q['id']
    assert q['explanation'] in text, q['id']
    assert all(c['explanation'] in text for c in q['choices']), q['id']
    assert all(r['url'] in text for r in q['references']), q['id']
    assert next(b for b in at.button if b.label == 'Submitted').disabled
    if (q.get('exhibit') or {}).get('kind') == 'code':
        assert any(c.value == q['exhibit']['content'] for c in at.code), q['id']
    if (q.get('exhibit') or {}).get('kind') == 'table':
        assert any(t.value.shape == (len(q['exhibit']['rows']),len(q['exhibit']['headers'])) for t in at.table), q['id']
    if q.get('diagram'):
        assert at.get('graphviz_chart'), q['id']
    for c in q['choices']:
        if '\n' in c['text']:
            assert any(code.value == c['text'] for code in at.code), q['id']


def run_all(limit=10):
    for n in range(1, limit+1):
        bank=load_bank(n); bid=bank['metadata']['set_id']; qs=bank['questions']
        validate_bank(bank)
        COUNT['validated_questions'] += len(qs)
        STORE.pop(bid,None)
        at=start(n)
        for q in qs:
            qid=q['id']
            jump(at,q)
            assert q['prompt'] in '\n'.join(m.value for m in at.markdown), qid
            assert q['explanation'] not in '\n'.join(m.value for m in at.markdown), qid
            click(at,'Submit answer')
            assert at.warning, qid
            assert qid not in at.session_state['progress']['submissions'], qid
            COUNT['empty_submission_rejected']+=1
            set_response(at,q,wrong(q))
            click(at,'Submit answer')
            assert at.session_state['progress']['submissions'][qid] == wrong(q), qid
            assert at.session_state['progress']['wrong_answers'][qid]['last_response'] == wrong(q), qid
            assert at.session_state['progress']['wrong_answers'][qid]['wrong_count'] == 1, qid
            check_reveal(at,q)
            COUNT['wrong_practice_submitted_and_revealed']+=1
            COUNT['types_'+q['type']]+=1
            if q.get('exhibit'): COUNT['exhibits_'+q['exhibit']['kind']]+=1
            if q.get('diagram'): COUNT['diagrams_rendered']+=1
            if len(at.session_state['progress']['submissions']) == 100:
                assert at.radio(key='view').value == 'Results & downloads'
                assert any('0/100' in s.value for s in at.success)
                at.radio(key='view').set_value('Practice');run(at)
            click(at,'Flag for review')
            assert qid in at.session_state['progress']['flags']
            COUNT['flag_persisted']+=1
        original=deepcopy(STORE[bid])
        assert len(original['submissions'])==len(original['flags'])==len(original['wrong_answers'])==100
        assert restore_progress(json.dumps(original),bank)==original
        COUNT['full_set_backup_roundtrips']+=1
        at=start(n)
        assert at.session_state['progress']==original
        COUNT['full_set_session_restores']+=1
        at.radio(key='view').set_value('Wrong-answer review');run(at)
        for q in qs:
            jump(at,q,review=True)
            set_response(at,q,answer(q),review=True)
            click(at,'Submit answer')
            check_reveal(at,q)
            p=at.session_state['progress']; entry=p['wrong_answers'][q['id']]
            assert entry['reviewed_at'] is not None and entry['wrong_count']==1
            assert entry['last_response']==wrong(q) and p['submissions'][q['id']]==wrong(q)
            COUNT['correct_review_preserves_score_and_wrong_history']+=1
        at.checkbox(key='confirm_reset').check();run(at);click(at,'Restart')
        p=at.session_state['progress']
        assert not p['submissions'] and not p['flags'] and len(p['wrong_answers'])==100
        COUNT['full_set_restarts_preserve_history']+=1
        for q in qs:
            jump(at,q)
            set_response(at,q,answer(q))
            click(at,'Submit answer')
            check_reveal(at,q)
            assert at.session_state['progress']['submissions'][q['id']]==answer(q)
            COUNT['correct_practice_submitted_and_revealed']+=1
        p=deepcopy(STORE[bid]);assert sum(is_correct(q,p['submissions'][q['id']]) for q in qs)==100
        assert len(p['wrong_answers'])==100 and all(e['reviewed_at'] for e in p['wrong_answers'].values())
        assert any('100/100' in s.value for s in at.success)
        assert restore_progress(json.dumps(p),bank)==p
        COUNT['full_set_backup_roundtrips']+=1
        prior=deepcopy(STORE)
        for other in range(1,11):
            if other == n:continue
            try: restore_progress(p,load_bank(other))
            except ValueError: COUNT['cross_set_backup_rejected']+=1
            else: raise AssertionError('cross-set restore accepted')
        at.selectbox(key='set_number').set_value(n%10+1);run(at)
        assert STORE[bid]==p
        at.selectbox(key='set_number').set_value(n);run(at)
        assert at.session_state['progress']==p
        COUNT['set_switch_roundtrips']+=1
        LEDGER['sets'].append({'set':n,'questions':100,'completed':True,'saved_bytes':len(json.dumps(p).encode()),'storage_writes':WRITES[bid]})
        save()
        print(f"Set {n:02d}: 100 wrong practice, 100 correct reviews, 100 correct practice; elapsed {time.monotonic()-START:.1f}s",flush=True)
    at=start(limit)
    at.radio(key='view').set_value('Overall results');run(at)
    metrics={m.label:m.value for m in at.metric}
    assert metrics['Submitted overall']==f'{limit*100} / 1,000'
    assert metrics['Accuracy overall']=='100.0%'
    assert metrics['Pending review']=='0'
    COUNT['overall_results_aggregation']+=1
    LEDGER['overall_metrics']=metrics
    save()

if __name__=='__main__':
    try:
        run_all(int(sys.argv[1]) if len(sys.argv)>1 else 10)
    except Exception as e:
        import traceback
        LEDGER['execution_error']={'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc()}
        save()
        raise
