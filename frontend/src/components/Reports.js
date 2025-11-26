import React,{useState} from 'react'
import {reportDaily, ledger} from '../api'

export default function Reports(){
  const [filters,setFilters] = useState({date_from:'',date_to:'',type:'',entity_code:''})
  const [rows,setRows] = useState([])
  const [ledgerData,setLedgerData] = useState(null)

  async function run(){
    const p={}
    if(filters.date_from) p.date_from = filters.date_from
    if(filters.date_to) p.date_to = filters.date_to
    if(filters.type) p.type = filters.type
    if(filters.entity_code) p.entity_code = filters.entity_code
    const d = await reportDaily(p)
    setRows(d)
    if(filters.entity_code){
      const l = await ledger(filters.entity_code,p)
      setLedgerData(l)
    }
  }

  return (
    <div>
      <div>
        <input type='date' onChange={e=>setFilters({...filters,date_from:e.target.value})}/>
        <input type='date' onChange={e=>setFilters({...filters,date_to:e.target.value})}/>
        <select onChange={e=>setFilters({...filters,type:e.target.value})}>
          <option value=''>All</option>
          <option value='Customer'>Customer</option>
          <option value='Supplier'>Supplier</option>
        </select>
        <input placeholder='Entity Code' onChange={e=>setFilters({...filters,entity_code:e.target.value})}/>
        <button onClick={run}>Run</button>
      </div>

      <h4>Daily Report</h4>
      <table border='1'>
        <thead><tr><th>Ref</th><th>Date</th><th>Code</th><th>Name</th><th>In</th><th>Out</th></tr></thead>
        <tbody>
          {rows.map(r=>(<tr key={r.ref_no}>
            <td>{r.ref_no}</td><td>{r.ref_date}</td><td>{r.entity_code}</td><td>{r.entity_name}</td><td>{r.in_amount}</td><td>{r.out_amount}</td>
          </tr>))}
        </tbody>
      </table>

      {ledgerData && (
        <>
        <h4>Ledger</h4>
        <table border='1'>
          <thead><tr><th>Ref</th><th>Date</th><th>In</th><th>Out</th><th>Balance</th></tr></thead>
          <tbody>
            {ledgerData.rows.map(r=>(<tr key={r.ref_no}>
              <td>{r.ref_no}</td><td>{r.ref_date}</td><td>{r.in_amount}</td><td>{r.out_amount}</td><td>{r.balance}</td>
            </tr>))}
          </tbody>
        </table>
        </>
      )}
    </div>
  )
}
