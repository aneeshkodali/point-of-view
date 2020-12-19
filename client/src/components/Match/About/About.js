import React from 'react';

import ScoreTable from './ScoreTable';

const About = ({ data }) => {

    // get variables from match data
    const { match, tournament, players } = data;



    // FORMAT DATE
    //get date object
    //const match_date_c = new Date(0)
    //match_date_c.setUTCSeconds(match.match_date['$date']/1000);
    // create date string
    //const match_date_year = match_date_c.getFullYear();
    //const month = match_date_c.getMonth()+1;
    //const match_date_month = month < 10 ? `0${month}` : month;
    //const day = match_date_c.getDate()+1;
    //const match_date_day = day < 10 ? `0${day}` : day;
    //const match_date_string = `${match_date_year}-${match_date_month}-${match_date_day}`;
   
    return (
        <div>
            <h1 className="ui header">{match.title}</h1>
            {/*<div>Date: {match_date_string}</div>*/}
            <div>Gender: {match.gender}</div>
            {/*<div>Tournament: {tournament.name}</div>*/}
            <div>Round: {match.match_round}</div>
            {/*<ScoreTable players={[winner, loser]} score={match.score} />*/}
        </div>
    );
}

export default About;