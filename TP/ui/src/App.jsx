import { Routes, Route } from 'react-router-dom'

import Home from './pages/Home'
import Invoice from './pages/Invoice'
import ErrorPage from './pages/ErrorPage'
import Root from './components/Root'

function App() {

  return (
    <>
    {/** Définitions des composants à loader en fonction des uris */}
      <Routes>
        {/** Root est toujours visible sur toutes les pages route parente */}
        <Route path="/" element={<Root />}>
          {/** les outlets qui vont s'intancier dans Outlet */}
          <Route index element={<Home />} />
          <Route path="invoice" element={<Invoice />} />
          <Route path="*" element={<ErrorPage />} />
        </Route>
      </Routes>
    </>
  )
}

export default App
