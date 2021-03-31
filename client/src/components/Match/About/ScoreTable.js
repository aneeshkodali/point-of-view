import React from 'react';

import { getCountryName } from '../../../helper/countries';

const ScoreTable = ({ data }) => {
    
    // get winner (0) and loser (1)
    const { players } = data
    const winner = players[0];
    const loser = players[1];

    // function to get flag icon from country 3 digit name
    const getFlagIcon = country => {
        const countryName = getCountryName(country).toLowerCase();
        return <i className={`${countryName} flag`} />;
    }

    // function to return name with abbreviated string
    const returnAbbreviatedName = name => {
        // split name
        const nameSplit = name.split(' ');
        // abbreviate first name
        nameSplit[0] = `${nameSplit[0][0].toUpperCase()}.`;
        
        return nameSplit.join(' ');
    }


    // initialize table data
    const tableHeaders = [
        <th key={'player'}>Player</th>
    ];
    const winnerData = [
        <td key={'winner'}>
            {getFlagIcon(winner['country'])}
            {returnAbbreviatedName(winner['full_name'])}
            <i className="ui check icon" />
        </td>
    ];
    const loserData = [
        <td key={'loser'}>
            {getFlagIcon(loser['country'])}
            {returnAbbreviatedName(loser['full_name'])}
        </td>
    ];

    // function to apply styling to set score if player won set
    // returns object of css properties
    const applyScoreStyling = (setScorePlayer, setScoreOpponent) => {

        const stylingObj = {};

        if (setScorePlayer > setScoreOpponent) {
            stylingObj['fontWeight'] = 'bold'
        }

        return stylingObj;
    }

    // loop through scores and append data accordingly
    const { sets } = data
    sets.forEach((set, index) => {

        let setWinner = set['players'][0]['full_name'];
        let setLoser = set['players'][1]['full_name'];

        const { players } = set['games'][set['games'].length-1];

        const setNum = set['set_in_match'];
        const setScoreWinner = players[0]['score']+1;
        const setScoreLoser = players[1]['score'];

        const winnerSetScore = winner['full_name'] === setWinner ? setScoreWinner : setScoreLoser;
        const loserSetScore = winner['full_name'] !== setWinner ? setScoreWinner : setScoreLoser;

        const winnerStylingObj = applyScoreStyling(winnerSetScore, loserSetScore);
        winnerStylingObj['backgroundColor'] = winnerSetScore > loserSetScore ? 'lightgreen' : '';
        const loserStylingObj = applyScoreStyling(loserSetScore, winnerSetScore);


        tableHeaders.push(
            <th key={setNum}>Set {setNum}</th>
        );
        winnerData.push(
            <td 
                key={setNum} 
                style={winnerStylingObj}
            >
                {winnerSetScore}
            </td>
        );
        loserData.push(
            <td 
                key={setNum} 
                style={loserStylingObj}
            >
                {loserSetScore}
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