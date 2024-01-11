import "./ChatMsgStyle.css";
import React, { useEffect, useRef } from 'react';

const ChatLayout = (props) => {
  const msgList = props.msgList;
  const containerRef = useRef();

  useEffect(() => {
    // Scroll to the bottom when messages change
    scrollToBottom();
  }, [msgList]);

  const scrollToBottom = () => {
    // Scroll to the bottom of the container
    if (containerRef.current) {
      // Scroll to the bottom of the container
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }  
  };

  if (msgList.length > 0) {
    const chatBubbles = msgList.map((obj, i) => (
      <div key={i} className={"bubbleContainer " + obj.direction}>
        <div className="bubble">
          <div className="button">{obj.message}</div>
        </div>
      </div>
    ));

    return (
      <div className="container" ref={containerRef}>
        {chatBubbles}
      </div>
    );
  }

  return <div className="container"></div>;
};

export default ChatLayout;
