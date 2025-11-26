import React, {useState} from 'react'
import {createMaster} from '../api'

export default function MasterForm(){
  const [form, setForm] = useState({entity_code:'',entity_name:'',addr1:'',addr2:'',type:'Customer',active:true})
  const [msg, setMsg] = useState(null)
  async function submit(e){
    e.preventDefault()
    const res = await createMaster(form)
    setMsg(res.entity_code ? 'Created '+res.entity_code : JSON.stringify(res))
  }
  return (
    <form onSubmit={submit}>
      <input placeholder='Entity Code' value={form.entity_code} onChange={e=>setForm({...form,entity_code:e.target.value})} required />
      <input placeholder='Entity Name' value={form.entity_name} onChange={e=>setForm({...form,entity_name:e.target.value})} required />
      <select value={form.type} onChange={e=>setForm({...form,type:e.target.value})}>
        <option>Customer</option>
        <option>Supplier</option>
      </select>
      <label>
        <input type='checkbox' checked={form.active} onChange={e=>setForm({...form,active:e.target.checked})}/>
        Active
      </label>
      <button>Create</button>
      {msg && <div>{msg}</div>}
    </form>
  )
}
