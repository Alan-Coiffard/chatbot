import React from "react";
import { Input, Button } from "@material-tailwind/react";
import SendIcon from '@mui/icons-material/Send';

const InputWithButton = (props) => {
  const [message, setMessage] = React.useState("");
  const onChange = ({ target }) => setMessage(target.value);
 
  return (
    <div className="relative flex w-full max-w-[24rem]">
      <Input
        type="text"
        label="Message"
        value={message}
        onChange={onChange}
        className="pr-20"
        containerProps={{
          className: "min-w-0",
        }}
      />
      <Button
        size="sm"
        color={message ? "gray" : "blue-gray"}
        disabled={!message}
        className="!absolute right-1 top-1 rounded"
        endIcon={<SendIcon />}
        onClick={console.log("dd")}
      >
        Send
      </Button>
    </div>
  );
}

export default InputWithButton;
