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
     {message && <p>{message}</p>}
     <button onClick={getData}>Click</button>
    </>
  )
}

export default App
