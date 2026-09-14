"""Exhaustive scorer and record contract using every question, independent of UI."""
import sys,json,itertools
from pathlib import Path
from collections import Counter
HERE = Path(__file__).resolve().parent
GENERATED = HERE / 'generated'
GENERATED.mkdir(exist_ok=True)
sys.path.insert(0,str(HERE.parent))
from quiz_core import load_bank,validate_bank,response_error,is_correct
from progress_store import empty_progress,record_answer,restart_attempt,restore_progress
from analytics import build_report
stats=Counter();banks=[];records={};per_question=[]
for n in range(1,11):
    bank=load_bank(n); validate_bank(bank);banks.append(bank)
    progress=empty_progress(bank)
    for q in bank['questions']:
        ids=[c['id'] for c in q['choices']]
        valid=0;right=0;wrong=None;cases=0
        if q['type']=='matching':
            pids=[p['id'] for p in q['pairs']]
            responses=(dict(zip(pids,values)) for values in itertools.product(ids,repeat=len(pids)))
            expected={p['id']:p['answer'] for p in q['pairs']}
        else:
            responses=(list(values) for length in range(len(ids)+1) for values in itertools.combinations(ids,length))
            expected=q['answer']
        for r in responses:
            cases+=1; stats['scoring_cases']+=1
            error=response_error(q,r)
            correct=is_correct(q,r)
            if error: assert not correct;stats['invalid_responses_rejected']+=1
            else:
                valid+=1; stats['valid_responses']+=1
                assert correct == (r==expected if q['type']=='matching' else set(r)==set(expected))
                if correct:right+=1;stats['correct_responses']+=1
                else:wrong=r;stats['wrong_responses']+=1
        assert right==1 and wrong is not None
        # Wrong first response, wrong retry, correct retry, later wrong reopens review.
        record_answer(progress,q,wrong,now='2026-09-14T00:00:00Z')
        assert progress['submissions'][q['id']]==wrong
        record_answer(progress,q,wrong,review=True,now='2026-09-14T00:01:00Z')
        assert progress['wrong_answers'][q['id']]['wrong_count']==2
        record_answer(progress,q,expected,review=True,now='2026-09-14T00:02:00Z')
        assert progress['wrong_answers'][q['id']]['reviewed_at']=='2026-09-14T00:02:00+00:00'
        record_answer(progress,q,wrong,review=True,now='2026-09-14T00:03:00Z')
        entry=progress['wrong_answers'][q['id']]
        assert entry['wrong_count']==3 and entry['reviewed_at'] is None and entry['last_response']==wrong
        assert progress['submissions'][q['id']]==wrong
        progress['flags'].append(q['id'])
        stats['full_wrong_correct_wrong_history_cycles']+=1
        per_question.append({'id':q['id'],'type':q['type'],'scoring_cases':cases,'valid_responses':valid,'correct_responses':right})
    assert restore_progress(json.dumps(progress),bank)==progress
    restart_attempt(progress)
    assert progress['submissions']=={} and progress['flags']==[] and len(progress['wrong_answers'])==100
    assert restore_progress(json.dumps(progress),bank)==progress
    records[bank['metadata']['set_id']]=progress
    stats['bank_restart_backup_roundtrips']+=1
report=build_report(banks,records)
assert report['totals']['answered']==0 and report['totals']['pending_review']==1000
assert report['totals']['wrong_attempts']==3000 and report['totals']['history_questions']==1000
out={'coverage':dict(stats),'questions':per_question,'totals_after_restart':report['totals']}
(GENERATED / 'core-results.json').write_text(json.dumps(out,indent=2))
(GENERATED / 'progress-fixtures.json').write_text(json.dumps(records,indent=2))
print(json.dumps(stats,indent=2))
