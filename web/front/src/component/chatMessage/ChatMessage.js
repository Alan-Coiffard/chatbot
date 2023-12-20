import "./ChatMsgStyle.css"

const ChatLayout = (props) => {
  const msgList = props.msgList;
//   const msgList = [
//     {
//         message: '1: This should be in left',
//         direction: 'left'
//     },
//     {
//         message: '2: This should be in right',
//         direction: 'right'
//     },
//     {
//         message: '3: This should be in left again',
//         direction: 'left'
//     }
// ];
  console.log(msgList);
  if(msgList != []) {
    const chatBubbles = msgList.map((obj, i = 0) => (
      <div className={"bubbleContainer " + obj.direction}>
          <div key={i++} className="bubble">
              <div className="button">{obj.message}</div>
          </div>
      </div>
    ));
    return <div className="container">{chatBubbles}</div>;
  }
  return <div className="container"></div>;

};

export default ChatLayout;