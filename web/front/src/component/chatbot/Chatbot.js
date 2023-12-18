import './Chatbot.css';
import Button from '@mui/material/Button';
import CloseIcon from '@mui/icons-material/Close';
import InputWithButton from "../inputWithButton/InputWithButton"

const Chatbot = (props) => {
    return (
        <div className="chatbot">
            <div className="header">
                Chatbot
                <Button
                    color="inherit"
                    endIcon={<CloseIcon />}
                    
                />            
            </div>
            <div className="conversation">
            </div>
            <form>
                <InputWithButton />
            </form>
        </div>
    );
};

export default Chatbot;
