import './Chatbot.css';
import CloseIcon from '@mui/icons-material/Close';
import ChatLayout from '../chatMessage/ChatMessage';
import React, { useState, useEffect } from 'react';
import { Input, Button } from "@material-tailwind/react";
import SendIcon from '@mui/icons-material/Send';
import "@fontsource/inter"; // Defaults to weight 400

const Chatbot = (props) => {

    const [msgList, setMsgList] = useState([]);
    const [connectionState, setConnectionState] = useState("Chatbot - Connection...");
    const [message, setMessage] = React.useState("");
    const onChange = ({ target }) => setMessage(target.value);
    
    const newSession = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/new`);
            const jsonData = await response.json();
            setConnectionState("Chatbot - " + jsonData['Connection'])
            setMsgList([
                ...msgList,
                ...jsonData["messages"]
            ]);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    useEffect(() => {
        newSession()
    }, []);

    const fetchData = async (msg, dir) => {
        setMsgList([
            ...msgList,
            { message: msg, direction: dir },
        ]);
        try {
            const lastItem = msgList[msgList.length - 1];
            console.log("lastitem", lastItem);
            if(lastItem['message'] === "what is the temperature?") msg = msg + " temperature"
            
            const response = await fetch(`http://localhost:5000/api/data?text=${msg}`);
            const jsonData = await response.json();
            
            if(jsonData.questionToAsk !== "") {
                let questionToAsk = []
                jsonData.questionToAsk.forEach(element => {
                    console.log(element);
                    questionToAsk.push({ message: element, direction: jsonData.direction });
                });
                setMsgList([
                    ...msgList,
                    { message: msg, direction: dir },
                    ...questionToAsk,
                ]);
            } else if (jsonData.info !== "") {
                let info = []
                jsonData.info.forEach(element => {
                    console.log(element);
                    info.push({ message: element, direction: jsonData.direction });
                });
                setMsgList([
                    ...msgList,
                    { message: msg, direction: dir },
                    ...info,
                ]);
            } else if (jsonData.listSymptoms !== "") {
                let listSymptoms = []
                jsonData.listSymptoms.forEach(element => {
                    console.log(element);
                    listSymptoms.push({ message: element, direction: jsonData.direction });
                });
                setMsgList([
                    ...msgList,
                    { message: msg, direction: dir },
                    { message: jsonData.message, direction: jsonData.direction },
                    { message: "You have : ", direction: jsonData.direction },
                    ...listSymptoms,
                ]);
            } else {
                setMsgList([
                    ...msgList,
                    { message: msg, direction: dir },
                    { message: jsonData.message, direction: jsonData.direction },
                ]);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div className="chatbot rounded-lg max-w-[24rem] w-[24rem]">
            <div className="header">
                {connectionState}
                <Button
                    color='white'
                    className="ml-1 p-2 border-0 shadow-2xl"
                >
                    <CloseIcon />
                </Button>            
            </div>
            <div className="conversation">
                <ChatLayout 
                    msgList={msgList} 
                />
            </div>
            <div className='form'>
                <div className="relative flex w-full">
                    <Input
                        type="text"
                        label="Message"
                        value={message}
                        onChange={onChange}
                        color='black'
                        className="pr-20 bg-white border-0"
                        containerProps={{
                            className: "min-w-0",
                        }}
                    />
                    <Button
                        size="sm"
                        variant='outlined'
                        disabled={!message}
                        className="!absolute right-1 top-1 rounded ml-1 p-1 shadow-2xl"
                        onClick={() => {
                            fetchData(message, 'right');
                            setMessage("");
                        }}
                    >
                        <SendIcon className='p-1' />
                    </Button>
                </div>
            </div>
        </div>
    );
};



export default Chatbot;
