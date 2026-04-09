const express = require('express');
const openai = require("openai");

const app=express();

const cors = require('cors')

app.use(cors())
app.use(express.json())

const mysql = require('mysql2/promises');

async function database() {

    const connection = mysql.createConnection({

  host: 'localhost',
  user: 'root',
  password: 'intern@123',
  database: 'voiceassistant'
})

const [rows]= await db.excecute("select * from fooditems")
await db.end()
return rows
}

app.get("/",async(req,res)=>{
    
    try{
    const rows=await database()
    res.json(rows)
    }
    catch(error){
        console.log(error+"error");
        res.status(500).json({error:error.message})
    }
    
})

app.post("/voice",(req,res)=>{
    const {transcript}=req.body;
    console.log("user said",transcript);
})

const client=new openai({
    apikey:"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",
    baseUrl:"https://api.groq.com/openai/v1"
})