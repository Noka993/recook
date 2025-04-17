// src/components/HeaderBackground.tsx

import React from 'react';
import '../assets/headerBackground.css';

interface HeaderBackgroundProps {
    text: string;
}

const HeaderBackground: React.FC<HeaderBackgroundProps> = ({ text }) => {
    return (
        <div className="header-background">{text}</div>
    );
}

export default HeaderBackground;
