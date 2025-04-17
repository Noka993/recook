import React from 'react';
import Header from '../../components/Header';  // Fixed typo in 'components'
import HomeBackground from '../../components/HomeBackground';  // Fixed typo in 'components'

const Home: React.FC = () => {
    return (
        <>
            <Header />
            <HomeBackground />
        </>
    );
}

export default Home;