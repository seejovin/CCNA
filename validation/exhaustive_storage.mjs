import assert from 'node:assert/strict';
import fs from 'node:fs';
const source=fs.readFileSync(new URL('../browser_storage.js',import.meta.url),'utf8');
const {default:render}=await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const collections=fs.readFileSync(new URL('../collection_storage.js',import.meta.url),'utf8');
const {default:readCollection}=await import(`data:text/javascript;base64,${Buffer.from(collections).toString('base64')}`);
const fixtures=JSON.parse(fs.readFileSync(new URL('./generated/progress-fixtures.json',import.meta.url),'utf8'));
const items=new Map();let writes=0;let loads=0;let saves=0;
Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:k=>items.get(k)??null,setItem(k,v){items.set(k,v);writes++}}});
Object.defineProperty(globalThis,'navigator',{configurable:true,value:{}});
const keys=Object.fromEntries(Object.keys(fixtures).map(bid=>[bid,`ccna:200-301:v1.1:set-${bid.slice(-2)}:progress:v1`]));
function send(host,bid,session_id,operation,payload){
  let result;
  const serialized=JSON.stringify(payload);
  render({parentElement:host,data:{session_id,storage_key:keys[bid],operation,request_id:operation==='load'?'load':serialized,serialized},setStateValue:(name,e)=>{assert.equal(name,'event');result=e}});
  return result;
}
for(const [bid,fixture] of Object.entries(fixtures)){
  const host={};assert.equal(send(host,bid,'active','load').status,'loaded');loads++;
  const payload={...fixture,wrong_answers:{}};
  for(const [qid,mistake] of Object.entries(fixture.wrong_answers)){
    payload.wrong_answers[qid]=mistake;
    const saved=send(host,bid,'active','save',payload);
    assert.equal(saved.status,'saved');saves++;
    const restored=send({},bid,'fresh-session','load');loads++;
    assert.deepEqual(restored.payload,payload);
    assert.deepEqual(restored.payload.wrong_answers[qid],mistake);
    for(const other of Object.keys(fixtures)){
      if(other===bid||!items.has(keys[other]))continue;
      assert.deepEqual(JSON.parse(items.get(keys[other])),fixtures[other]);
    }
  }
  assert.deepEqual(JSON.parse(items.get(keys[bid])),fixture);
}
let snapshot;
readCollection({parentElement:{},data:{session_id:'all',request_id:'fresh',storage_keys:keys},setStateValue:(name,event)=>snapshot=event});
assert.deepEqual(snapshot.records,fixtures);assert.deepEqual(snapshot.errors,{});
const result={passed:true,question_history_incremental_saves:saves,fresh_component_loads:loads,sets:items.size,collection_snapshot_questions:Object.values(snapshot.records).reduce((n,p)=>n+Object.keys(p.wrong_answers).length,0),writes,total_stored_utf16_bytes:[...items.values()].reduce((n,s)=>n+s.length*2,0)};
fs.writeFileSync(new URL('./generated/storage-results.json',import.meta.url),JSON.stringify(result,null,2));
console.log(result);
