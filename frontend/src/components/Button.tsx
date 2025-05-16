import React from "react";

interface ButtonProps {
  id: string;
  link: string;
  text: string;
}

const Button: React.FC<ButtonProps> = ({ id, link, text }) => {
  return (
    <a
      href={link}
      id={id}
      className="inline-flex items-center justify-center px-8 py-4 text-white text-xl md:text-2xl 
      font-bold bg-[var(--color-primary)] 
      rounded-[30px_20px] transition-all duration-200 hover:bg-[#477935] no-underline"
    >
      {text}
    </a>
  );
};

export default Button;
