import React from 'react';
import '../assets/iconTextSection.css';

interface IconTextSectionProps {
    icon: string;
    text: string;
}

const IconTextSection: React.FC<IconTextSectionProps> = ({ icon, text }) => {
    return (
        <div className="icon-text-section">
            <img src={icon} alt="icon" />
            {text}
        </div>
    );
}

export default IconTextSection;
