import { Link } from 'react-router-dom'
import '../App.css'

function Posts() {

  return (
    <>
         <h1>Hello Posts</h1>
         <ul>
         {[1,2,3].map((postId, i) => <li key={i}><Link to={`/post/${postId}`} >{postId}</Link></li>  )}
         </ul>
      
    </>
   
  )
}

export default Posts
