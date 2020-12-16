import React from 'react';

const Summary = ({ matchData }) => {

    const { match_date, winner, loser, score, result } = matchData;

    return (
        <div>
            <div>Result: {result}</div>
        </div>
    );
}

export default Summary;