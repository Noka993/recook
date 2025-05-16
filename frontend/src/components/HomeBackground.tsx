import React from "react";
import Divider from "./Divider";

const HomeBackground: React.FC = () => {
  return (
    <div
      className="overflow-hidden w-full min-h-[90vh] bg-cover bg-center bg-no-repeat text-white font-['Inter'] flex flex-col justify-center items-center"
      style={{ backgroundImage: `url('/meal1.jpg')` }}
    >
      {/* Overlay */}
      <div className="w-full h-96 bg-[rgba(155,155,155,0.4)] p-10 flex flex-col justify-center items-center text-center backdrop-blur-sm">
        <h1 className="text-5xl md:text-6xl font-bold mb-4">RECOOK</h1>
        <Divider />
        <p className="font-['Inria Serif'] text-3xl md:text-4xl max-w-3xl mt-6">
          A PLACE TO SHARE YOUR TASTE. RECOOK IS A RECIPE SHARING PLATFORM
        </p>
      </div>

      {/* Discover Button */}
      <a
        href="/recipes"
        className="mt-10 sm:mt-16 px-8 py-4 
        sm:px-10 sm:py-5 text-lg sm:text-xl md:text-2xl 
        font-bold text-white bg-[var(--primary-color)] 
        rounded-[30px_20px] transition-all duration-200 hover:bg-[#477935] hover:text-[var(--text-hover)]"
      >
        DISCOVER
      </a>
    </div>
  );
};

export default HomeBackground;
