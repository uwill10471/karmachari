import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {

const[message,setMessage]= useState("")
const getData = async()=>{
     try{

         const response = await axios.get(" http://127.0.0.1:5000/data")
         console.log(response.data.message)
         setMessage(response.data.message)

      }catch(e){
           console.error("Error getting Data", e)

       }

    }
  return (
    <>
 <div className="container">
     <div className="vertical-line"></div>


 </div>
 <h4 className="v-l-text">SLIDE</h4>
<nav className="Home-nav">
<ul className="Home-nav-ul" type="circle">
    <li className="Home-nav-ul-li">Home</li>
    <li className="Home-nav-ul-li">Artists</li>
    <li className="Home-nav-ul-li">Contact</li>
    <li className="Home-nav-ul-li">Terms and Conditions</li>
</ul>
</nav>

<div className="Home-image">
    <img src="../public/delLater10.png" alt="image" height="100px"/>
 </div>

<div className="container-vertical-line">
      <div className="vertical-line-bottom"></div>
</div>
 <h4 className="v-l-text-bottom">Create Art</h4>

 <div className="v-l-b-right">
     <div className="vertical-line-bottom-right"></div>
     </div>
<h4 className="v-l-text-bottom-right">Gallery</h4>

        <div className="explore"><button className="explore-btn">Explore Now</button></div>
    </>
  )
}

export default App
