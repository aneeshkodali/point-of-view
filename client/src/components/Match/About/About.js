import React from 'react';

import { convertDate } from '../../../helper/functions';
import ScoreTable from './ScoreTable';

const About = ({ matchData }) => {

    // get variables from match data
    const { title, gender, match_date, match_round, score, tournament, players, winner, loser } = matchData;
   
    return (
        <div>
            <h1 className="ui header">{title}</h1>
            <div>Date: {convertDate(match_date)}</div>
            <div>Gender: {gender}</div>
            <div>Tournament: {tournament.name}</div>
            <div>Round: {match_round}</div>
            <ScoreTable players={[winner, loser]} score={score} />
        </div>
    );
}

export default About;