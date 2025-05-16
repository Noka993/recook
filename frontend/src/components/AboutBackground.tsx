import React from "react";
import Divider from "./Divider";
import Button from "./Button";
import SectionHeader from "./SectionHeader";

const AboutBackground: React.FC = () => {
  return (
    <div className="flex flex-nowrap w-full min-h-[90vh] flex-col md:flex-row">
      {/* Banner section */}
      <div className="flex-2 w-full md:w-auto bg-[rgb(116,78,56)] md:min-h-4/5" />

      {/* About content section */}
      <div className="flex-3 bg-[var(--secondary-color)] flex flex-col items-center justify-center px-4 py-12 text-center gap-8">
        <SectionHeader text="ABOUT US" />
        <Divider />

        <div className="max-w-3xl font-['Inria_Serif'] text-lg sm:text-xl space-y-6">
          <p>
            This website was made with love by Miłosz Malinowski. I am a
            Computer Science student at Warsaw University of Life Sciences. It
            is an attempt to showcase my web development skills.
          </p>
          <p>
            This is my final project for Harvard’s CS50 course. I used the
            following technologies: <b>React</b> with pure <b>CSS</b>,{" "}
            <b>Flask</b>, <b>SQLAlchemy</b>.
          </p>
        </div>

        <Divider />
        <Button link="/about" text="LEARN MORE" id="about-button" />
      </div>
    </div>
  );
};

export default AboutBackground;
