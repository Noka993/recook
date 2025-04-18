import React from 'react';
import Divider from './Divider';
import Button from './Button';
import SectionHeader from './SectionHeader';
import '../assets/aboutBackground.css';

const AboutBackground: React.FC = () => {
  return (
    <div className="about-background">
      <div className="banner"></div>
      <div className="about-section">
        <SectionHeader text="ABOUT US" />
        <Divider />
        <div className="section-content">
          <p>
            This website was made with love by Miłosz Malinowski. I am a Computer Science student at Warsaw University of Life Sciences. It is an attempt to showcase my web development skills
          </p>

          <p>
            This is my final project for Harvard’s CS50 course. I used the following technologies: <b>React </b>with pure <b>CSS, Flask, SQLAlchemy</b>
          </p>
        </div>
        <Divider />
        <Button link="/about" text="LEARN MORE" id="about-button" />
      </div>
    </div>
  );
}

export default AboutBackground;