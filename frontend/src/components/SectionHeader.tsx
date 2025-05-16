import React from "react";

interface SectionHeaderProps {
  text: string;
}

const SectionHeader: React.FC<SectionHeaderProps> = ({ text }) => {
  return (
    <div
      className="
      bg-[var(--background-secondary)] 
      text-white 
      flex 
      items-center 
      justify-center 
      font-bold 
      w-full
      mb-5
      max-w-[900px] 
      h-[160px]
      min-h-[120px]
      px-4
      text-3xl
      md:text-4xl
      "
    >
      {text}
    </div>
  );
};

export default SectionHeader;
