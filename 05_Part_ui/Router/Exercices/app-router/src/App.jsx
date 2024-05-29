import {  Routes, Route } from 'react-router-dom'
import './App.css'
import Posts from './components/Posts'
import Home from './components/Home'
import Contact from './components/Contact'
import Root from './routes/root'
import ErrorPage from './components/error-page'
import Post from './components/Post'

function App() {
  // le composant principal on définit la logique du chargement des routes
  // dans index c'est le composant chargé par défaut correspond à l'adresse /

  return (
    <>
      <Routes>
          <Route path="/" element={<Root />}>
          <Route index element={<Home />} />
          <Route path="posts" element={ <Posts />} />
          <Route path="contact" element={ <Contact />} />
          <Route path="post/:postId" element={ <Post />} />
          <Route path="*" element={<ErrorPage />} />
        </Route>
      </Routes>
    </>
  )
}

export default App
