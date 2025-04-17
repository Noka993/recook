import React from 'react';
import '../assets/header.css';

const Header: React.FC = () => {
    return (
        <div className="nav-bar">
            <div className="menu-logo">
                <p className="logo-text"><a id="nav-a" href='/'>RECOOK</a></p>
            </div>
            <div className="menu">
                <div className="menu-item"><a id="nav-a" href='/about'>ABOUT</a></div>
                <div className="menu-item"><a id="nav-a" href='/contact'>CONTACT</a></div>
                <div className="menu-item"><a id="nav-a" href='/register'>SIGN UP</a></div>
                <div className="menu-item"><a id="nav-a" href='/login'>LOGIN</a></div>
            </div>
        </div>
    );
}

export default Header;