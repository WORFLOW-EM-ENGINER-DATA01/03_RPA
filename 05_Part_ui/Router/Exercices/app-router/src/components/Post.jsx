import '../App.css'
import {  useParams } from 'react-router-dom';

function Post(props) {
    const { postId } = useParams(); 

    console.log()

  return (
    <>
      <h1>Post --  {postId} </h1>
    </>
  )
}

export default Post
