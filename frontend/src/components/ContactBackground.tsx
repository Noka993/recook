import React from 'react';
import Divider from './Divider';
import Button from './Button';
import SectionHeader from './SectionHeader';
import InputField from './InputField';
import IconTextSection from './IconTextSection';
import '../assets/aboutBackground.css';

const ContactBackground: React.FC = () => {
    return (
        <div className="about-background">
            <div className="about-section">
                <SectionHeader text="CONTACT" />
                <IconTextSection icon="/assets/email.png" text="7lO4l@example.com" />
                <IconTextSection icon="/assets/phone.png" text="123-456-789" />
                <Divider />
                <div className="message-form">
                    <InputField type="text" placeholder="NAME" />
                    <InputField type="email" placeholder="EMAIL" />
                    <InputField type="text" placeholder="MESSAGE" />
                    <Button link="#" text="SEND" id="send-button" />
                </div>
            </div>
            <div className="banner"></div>
        </div>
    );
}

export default ContactBackground;