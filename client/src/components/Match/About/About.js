import React from 'react';

import ScoreTable from './ScoreTable';

const About = ({ matchData }) => {

    // get variables from data
    const { match_date, gender, tournament, match_round, title, result, winner, loser, score, sets } = matchData;

    // FORMAT DATE
    //get date object
    const match_date_c = new Date(0)
    match_date_c.setUTCSeconds(match_date['$date']/1000);
    // create date string
    const match_date_year = match_date_c.getFullYear();
    const month = match_date_c.getMonth()+1;
    const match_date_month = month < 10 ? `0${month}` : month;
    const day = match_date_c.getDate()+1;
    const match_date_day = day < 10 ? `0${day}` : day;
    const match_date_string = `${match_date_year}-${match_date_month}-${match_date_day}`;

   
    return (
        <div>
            <h1 className="ui header">{title}</h1>
            <div>Date: {match_date_string} VERIFY THIS</div>
            <div>Gender: {gender}</div>
            <div>Tournament: {tournament['$oid']}</div>
            <div>Round: {match_round}</div>
            <div>Result: {result}</div>
            <div>Winner: {winner['$oid']}</div>
            <div>Loser: {loser['$oid']}</div>
            <div>Score: {score}</div>
            <div>:Sets: {sets}</div>

            <ScoreTable />
        </div>
    );
}

export default About;