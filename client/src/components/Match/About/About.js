import React from 'react';

import ScoreTable from './ScoreTable';

const About = ({ matchData }) => {

    // get variables from match data
    const { title, gender, match_date, match_round, score, tournament, players, winner, loser } = matchData;

    const getPlayerData = (player, playerArr) => {
        return players.filter(p => p['_id']['$oid'] == player['$oid'])[0];
    }

    // get winner
    const winnerData = getPlayerData(winner, players);
    const loserData = getPlayerData(loser, players);



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
            <div>Date: {match_date_string}</div>
            <div>Gender: {gender}</div>
            <div>Tournament: {tournament.name}</div>
            <div>Round: {match_round}</div>
            <ScoreTable players={[winnerData, loserData]} score={score} />
        </div>
    );
}

export default About;