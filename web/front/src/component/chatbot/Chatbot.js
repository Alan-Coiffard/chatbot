import './Chatbot.css';
import CloseIcon from '@mui/icons-material/Close';
import ChatLayout from '../chatMessage/ChatMessage';
import React, { useState } from 'react';
import { Input, Button } from "@material-tailwind/react";
import SendIcon from '@mui/icons-material/Send';
import "@fontsource/inter"; // Defaults to weight 400

const Chatbot = (props) => {
    const [msgList, setMsgList] = useState([
        {
                    message: '1: This should be in left',
                    direction: 'left'
                },
                {
                    message: '2: This should be in right',
                    direction: 'right'
                },
                {
                    message: '3: This should be in left again',
                    direction: 'left'
                }
    ]);
    const [message, setMessage] = React.useState("");
    const onChange = ({ target }) => setMessage(target.value);


    return (
        <div className="chatbot rounded-lg">
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
                <ChatLayout msgList={msgList} />
            </div>
            <div className='form'>
                <div className="relative flex w-full max-w-[24rem]">
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
                            setMsgList([
                                ...msgList,
                                { message: message, direction: 'right' }
                            ]);
                            setMessage("")
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
