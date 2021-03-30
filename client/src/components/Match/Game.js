import React from 'react';

const Game = ({ data }) => {

    // store text to display
    const textToDisplay = "To start, simply count the number of times you and your opponent end the point a certain way.";

    // create array of player-outcome counts
    const resultCounts = [];
    const pointsWonCounts = []
    const players = data['players'].map(player => player['full_name']);
    const results = ['ace', 'double fault', 'forced error', 'service winner', 'unforced error', 'winner'];
    players.forEach(player => {
        results.forEach(result => {
            let resultObj = {};
            resultObj['player'] = player;
            resultObj['result'] = result;
            resultObj['count'] = 0;
            resultCounts.push(resultObj);
            pointsWonCounts.push(resultObj);
        });
    });
    
    data['sets'].forEach(set => {
        set['games'].forEach(game => {
            game['points'].forEach(point => {

                point['shots'].forEach(shot => {

                    const { result, shot_by } = shot;
                    if (results.includes(result)) {
                        resultCounts.filter(resultObj => (resultObj['player'] === shot_by) && (resultObj['result'] === result))[0]['count'] ++;
                    }
                });
            });
        });
    });

    console.log(resultCounts);
    console.log(pointsWonCounts);


    return (
        <div>
            {textToDisplay}
        </div>
    );
}

export default Game;