import React from 'react';
import '../assets/sectionHeader.css';

interface SectionHeaderProps {
    text: string;
}

const SectionHeader: React.FC<SectionHeaderProps> = (props) => {
    return (
        <div className="section-header">
            {props.text}
        </div>
    );
}

export default SectionHeader;
