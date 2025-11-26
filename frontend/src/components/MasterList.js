import React, {useEffect, useState} from 'react'
import {listMasters} from '../api'

export default function MasterList(){
  const [rows,setRows] = useState([])
  useEffect(()=>{ listMasters().then(setRows) },[])
  return (
    <table border='1'>
      <thead><tr><th>Code</th><th>Name</th><th>Type</th><th>Status</th></tr></thead>
      <tbody>
        {rows.map(r=>(<tr key={r.entity_code}>
          <td>{r.entity_code}</td><td>{r.entity_name}</td><td>{r.type}</td><td>{r.active?'Active':'Inactive'}</td>
        </tr>))}
      </tbody>
    </table>
  )
}
