import React, {useState} from 'react'
import MasterList from './components/MasterList'
import MasterForm from './components/MasterForm'
import TransactionForm from './components/TransactionForm'
import Reports from './components/Reports'

export default function App(){
  const [view, setView] = useState('masters')
  return (
    <div style={{padding:20}}>
      <h2>Master-Transaction App</h2>
      <nav>
        <button onClick={()=>setView('masters')}>Masters</button>
        <button onClick={()=>setView('transactions')}>Transactions</button>
        <button onClick={()=>setView('reports')}>Reports</button>
      </nav>
      <hr/>
      {view==='masters' && <><MasterForm/><MasterList/></>}
      {view==='transactions' && <TransactionForm/>}
      {view==='reports' && <Reports/>}
    </div>
  )
}
