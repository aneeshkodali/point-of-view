import React from 'react';

import { getCountryName } from '../../../helper/countries';

const ScoreTable = ({ matchData }) => {
    
    // get winner (0) and loser (1)
    const { players } = matchData
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
            {getFlagIcon(winner['country_id']['country'])}
            {returnAbbreviatedName(winner['full_name'])}
            <i className="ui check icon" />
        </td>
    ];
    const loserData = [
        <td key={'loser'}>
            {getFlagIcon(loser['country_id']['country'])}
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
    const { sets } = matchData
    sets.forEach((set, index) => {

        const { players } = set['games'][set['games'].length-1];

        const setNum = index+1;
        const setScoreWinner = players[0]['score']+1;
        const setScoreLoser = players[1]['score'];

        const winnerStylingObj = applyScoreStyling(setScoreWinner, setScoreLoser);
        winnerStylingObj['backgroundColor'] = setScoreWinner > setScoreLoser ? 'lightgreen' : '';
        const loserStylingObj = applyScoreStyling(setScoreLoser, setScoreWinner);


        tableHeaders.push(
            <th key={setNum}>Set {setNum}</th>
        );
        winnerData.push(
            <td 
                key={setNum} 
                style={winnerStylingObj}
            >
                {setScoreWinner}
            </td>
        );
        loserData.push(
            <td 
                key={setNum} 
                style={loserStylingObj}
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