import './Chatbot.css';
import CloseIcon from '@mui/icons-material/Close';
import ChatLayout from '../chatMessage/ChatMessage';
import React, { useState } from 'react';
import { Input, Button } from "@material-tailwind/react";
import SendIcon from '@mui/icons-material/Send';
import "@fontsource/inter"; // Defaults to weight 400

const Chatbot = (props) => {
    const chatBotName = 'OncologyAid'
    const emergencyList = [
        "42°c fever",
        " stroke"
    ]
    const [msgList, setMsgList] = useState([
        {
            message: 'Welcome to ' + chatBotName + ' !',
            direction: 'left'
        },
        {
            message: 'If you are experiencing emergency symptoms such as : '+ emergencyList +', please call your medical provider as soon as possible.',
            direction: 'left'
        },
        {
            message: 'What can I do for you ?',
            direction: 'left'
        },
    ]);
    const [message, setMessage] = React.useState("");
    const onChange = ({ target }) => setMessage(target.value);
    
    const fetchData = async (msg, dir) => {
        setMsgList([
            ...msgList,
            { message: msg, direction: dir },
        ]);
        try {
            const response = await fetch(`http://localhost:5000/api/data?text=${msg}`);
            const jsonData = await response.json();
            if (jsonData.info !== "") {
                let info = []
                jsonData.info.forEach(element => {
                    console.log(element);
                    info.push({ message: element, direction: jsonData.direction });
                });
                setMsgList([
                    ...msgList,
                    { message: msg, direction: dir },
                    { message: jsonData.message, direction: jsonData.direction },
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
        <div className="chatbot rounded-lg max-w-[20rem] w-[20rem]">
            <div className="header">
                Chatbot
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
