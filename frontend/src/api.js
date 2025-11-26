const API = 'http://localhost:8000'

export async function listMasters(){
  const r = await fetch(`${API}/masters`)
  return r.json()
}
export async function createMaster(body){
  const r = await fetch(`${API}/masters`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(body)})
  return r.json()
}
export async function createTransaction(body){
  const r = await fetch(`${API}/transactions`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(body)})
  return r.json()
}
export async function reportDaily(params){
  const qs = new URLSearchParams(params)
  const r = await fetch(`${API}/reports/daily?${qs.toString()}`)
  return r.json()
}
export async function ledger(entity_code, params){
  const qs = new URLSearchParams(params)
  const r = await fetch(`${API}/reports/ledger?entity_code=${entity_code}&${qs.toString()}`)
  return r.json()
}
