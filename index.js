const express = require('express');
const openai = require("openai");

const app=express();

const cors = require('cors')

app.use(cors())
app.use(express.json())

const mysql = require('mysql2/promises');
const { Models } = require('groq-sdk/resources/models.js');

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

async function run(){
    try{
        const prompt=`your hotel booking assistant for echoChats. the user said: "${transcript}"
    

    important rules
    1. the user may say multiple things in one sentance
    2. you must respond Last command you detect
    3. ignore all previous commands
    4. donot mention any other commands in your response

    example
    user : "show me business hotels show me luxary hotels"--> Respond to "show me business hotels" Only
    user : "show me luxary hotels show me business hotels"--> Respond to "show me luxary hotels" Only

    available hotels in our database

    Grand Palace Hotel (₹4500) – Luxury
    Sea Breeze Resort (₹6200) – Resort
    Mountain View Inn (₹3200) – Budget
    City Comfort Stay (₹2400) – Business
    Royal Heritage Hotel (₹7200) – Heritage
    Budget Inn (₹1500) – Budget
    Lake View Resort (₹6800) – Resort
    Business Hub Hotel (₹5200) – Business
    Urban Stay Suites (₹3900) – Apartment
    Airport Express Hotel (₹2800) – Transit
    Sunrise Residency (₹2100) – Budget
    Elite Grand Hotel (₹9500) – Luxury
    Comfort Living Hotel (₹3400) – Mid-range
    Palm Grove Resort (₹7700) – Resort
    Metro City Lodge (₹1800) – Budget

based on the usersvoice inout, respond one of those command types:

1. if user want to filter by category(business,budeget,Transit,Luxary)
{
"command":"FILTER"
"category":"Business" or "luxary","Budget","Resort"
"response":"showing all your Luxary hotels"
}

2. if user want to navigate to a Page

{
"command":"NAVIGATE",
"page":"home" or "about" or "hotels" or "my bookings" or "login"
"path":"/" or "/home" or "/about" or "/hotels" or "/my bookings" or "/login"
"response":"taking you to home page"
}

3. if user want to LOGIN
{
"command":"NAVIGATE"
"page":"login"
"path":"/login"
"response":"taking you to the login page"
}

4. wants to LOGOUT

{
"command":"LOGOUT"
"response":"logging you out"
}

5. if user wants to BOOK hotel

{
"command":"BOOK"
hotels:[
        {
        "name":"Exact hotel name"
        "rooms":"exact room type"
        "price":"number"
        }
        "response":"confirm your booking"
     ]
}

6. if user want to cancel cancel the booking
{
"command":"CANCEL"
"hotels":[
         {
            "name":"Exact hotel name"
            "rooms":"exact room type"
            }
         ]
         "response":"Yor room is cancelled"
         }

7. if the command is unclear
{
        command:"UNKNOWN"
        response:"i didnt understand please repeat"
}
        Return only the JSON object , no additional text.
`
        const response= await client.chat.completions.create(
            {
            Model : "ll.3.3-70b-versatile",
            message :[
                {
                    role:"system",
                    content:"you are always helpful hotel booking assistant. alwyas respond with valid JSON"
                }
            ],
            temperature:0.7,
            max_tokens:500
        }
        )
        console.log("ai response :",response.choices[0].message.content);

        let commanddata
        try{
            commanddata= JSON.parse(response.choices[0].message.content)
        }
        catch{
            commanddata={
                command:"UNKNOWN",
                response:response.choices[0].message.content
            }
        }
        res.json({
            status:"Booking Successful👍",
            transcript:transcript,
            aiResponse:commanddata
        })
    }
    catch(error){
        console.error("error",error)
        res.status(500).json({error:"fail to process to voice command"})
    }
}
run()