import { useEffect, useState } from 'react'


function App() {
  const [invoices, setInvoices] = useState([])

  useEffect(() => {
    async function get(){
    const response = await fetch('http://localhost:8002/api/invoices')
    const invoices = await response.json()
    setInvoices(invoices)
    }
    get()
  }, [])

  return (
    <>
      { invoices && invoices.map((invoice) => <p key={invoice.id}>{invoice.trainer}</p> ) }
    </>
  )
}

export default App
