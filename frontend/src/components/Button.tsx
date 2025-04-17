import React from 'react';
import '../assets/button.css';

interface ButtonProps {
  id: string;
  link: string;
  text: string;
}

const Button: React.FC<ButtonProps> = ({ id, link, text }) => {
  return (
    <button className="btn-default" id={id}>
      <a href={link}>{text}</a>
    </button>
  );
}

export default Button;
