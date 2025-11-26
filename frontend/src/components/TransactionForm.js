import React, {useEffect, useState} from 'react'
import {listMasters, createTransaction} from '../api'

export default function TransactionForm(){
  const [masters,setMasters] = useState([])
  const [form,setForm] = useState({transaction_number:'',transaction_date:'',entity_code:'',amount:0})
  const [msg,setMsg] = useState(null)

  useEffect(()=>{ listMasters().then(m=>setMasters(m.filter(x=>x.active))) },[])

  async function submit(e){
    e.preventDefault()
    const res = await createTransaction(form)
    setMsg(res.ref_no ? 'Saved '+res.ref_no : JSON.stringify(res))
  }

  return (
    <form onSubmit={submit}>
      <input placeholder='Txn No' value={form.transaction_number} onChange={e=>setForm({...form,transaction_number:e.target.value})} required/>
      <input type='date' value={form.transaction_date} onChange={e=>setForm({...form,transaction_date:e.target.value})} required/>
      <select value={form.entity_code} onChange={e=>setForm({...form,entity_code:e.target.value})} required>
        <option value=''>Select Entity</option>
        {masters.map(m=>(<option key={m.entity_code} value={m.entity_code}>{m.entity_name}</option>))}
      </select>
      <input type='number' step='0.01' value={form.amount} onChange={e=>setForm({...form,amount:parseFloat(e.target.value)})} required/>
      <button>Save</button>
      {msg && <div>{msg}</div>}
    </form>
  )
}
