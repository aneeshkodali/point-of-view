import React from 'react';

const ScoreTable = ({ players, score }) => {

    // get winner (0) and loser (1)
    const winner = players[0];
    const loser = players[1];

    // split score - sets separated by ' , scores separated by '-'
    const scoreSplit = score.split(' ').map(set => set.split('-'));

    // initialize table data
    const tableHeaders = [
        <th key={'player'}>Player</th>
    ];
    const winnerData = [
        <td key={'winner'}>{winner}</td>
    ];
    const loserData = [
        <td key={'loser'}>{loser}</td>
    ];

    // function to apply styling to set score if player won set
    // returns object of css properties
    const applyScoreStyling = (setScorePlayer, setScoreOpponent) => {
        if (setScorePlayer > setScoreOpponent) {
            return {
                'fontWeight': 'bold',
                'backgroundColor': 'lightgreen'
            }
        }
    }

    // loop through scores and append data accordingly
    scoreSplit.forEach((set, index) => {

        const setNum = index+1;
        const setScoreWinner = set[0];
        const setScoreLoser = set[1];

        tableHeaders.push(
            <th key={setNum}>Set {setNum}</th>
        );
        winnerData.push(
            <td 
                key={setNum} 
                style={applyScoreStyling(setScoreWinner, setScoreLoser)}
            >
                {setScoreWinner}
            </td>
        );
        loserData.push(
            <td 
                key={setNum} 
                style={applyScoreStyling(setScoreLoser, setScoreWinner)}
            >
                {setScoreLoser}
            </td>
        )
    });

    // combine data
    const tableData = [winnerData, loserData].map((row, index) => {
        const keyVal = row[0].props.children;
        return (
            <tr 
                key={keyVal}
            >
                {row}
            </tr>
        );
    });

    return (
        <div>
            <table className="ui celled table">
                <thead>
                    <tr>
                        {tableHeaders}
                    </tr>
                </thead>
                <tbody>
                    {tableData}
                </tbody>
            </table>
        </div>
    );
}

export default ScoreTable;