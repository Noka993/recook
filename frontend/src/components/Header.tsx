import React from "react";
import "../assets/header.css";

const Header: React.FC = () => {
  return (
    <div className="md:min-h-[10vh] flex items-center justify-between p-6 text-white w-full bg-[var(--color-primary)]">
      <div className="flex-auto mr-10">
        <p className="md:text-4xl text-2xl font-bold">
          <a id="nav-a" href="/">
            RECOOK
          </a>
        </p>
      </div>
      <div className="flex md:gap-x-10 gap-x-4 md:text-2xl text-[16px] font-medium whitespace-nowrap">
        <div className="menu-item">
          <a id="nav-a" href="/about" className="hover:text-gray-200">
            ABOUT
          </a>
        </div>
        <div className="menu-item">
          <a id="nav-a" href="/contact" className="hover:text-gray-200">
            CONTACT
          </a>
        </div>
        <div className="menu-item">
          <a id="nav-a" href="/register" className="hover:text-gray-200">
            SIGN UP
          </a>
        </div>
        <div className="menu-item">
          <a id="nav-a" href="/login" className="hover:text-gray-200">
            LOGIN
          </a>
        </div>
      </div>
    </div>
  );
};

export default Header;
