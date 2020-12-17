import React from 'react';

const About = ({ matchData }) => {

    const { title, match_date, winner, loser, score, result } = matchData;

    return (
        <div>
            <h1 className="ui header">{title}</h1>
            <div>Result: {result}</div>
        </div>
    );
}

export default About;