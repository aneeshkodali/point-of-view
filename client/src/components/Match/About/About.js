import React from 'react';

import { convertDate, convertHeight } from '../../../helper/functions';
import ScoreTable from './ScoreTable';

const About = ({ matchData }) => {

    // get variables from match data
    const { title, gender, match_date, match_round, score, tournament, players, winner, loser } = matchData;


    // function to create player card
    const createPlayerCard = player => {
        const id = player['_id']['$oid'];
        const { full_name, image_url, country, backhand, date_of_birth, hand, height } = player;
        return (
            <div key={id} className="ui card">
                <div className="content">
                    <div className="center aligned header">{full_name} ({country})</div>
                </div>
                <div>
                    <img className="ui centered image" src={image_url} alt={full_name} />
                </div>
                <div className="content">
                    <div className="description">
                        <span className="right floated">Height: {convertHeight(height)}</span>
                        Born: {convertDate(date_of_birth)}
                    </div>
                    <div className="description">
                        <span className="right floated">Backhand: {backhand}</span>
                        Plays: {hand}
                    </div>
                </div>
            </div>
        );
    }

    const matchInfo = (
        <div>
            <div>Date: {convertDate(match_date)}</div>
            <div>Gender: {gender}</div>
            <div>Tournament: {tournament.name}</div>
            <div>Round: {match_round}</div>
            <ScoreTable players={[winner, loser]} score={score} />
        </div>
    );
   
    return (
        <div>
            <div className="ui grid">
                <div className="row">
                    <div className="five wide column">{createPlayerCard(players[0])}</div>
                    <div className="six wide column">{matchInfo}</div>
                    <div className="five wide column">{createPlayerCard(players[1])}</div>
                </div>
            </div>
            {/*<h1 className="ui header">{title}</h1>
            <div>Date: {convertDate(match_date)}</div>
            <div>Gender: {gender}</div>
            <div>Tournament: {tournament.name}</div>
            <div>Round: {match_round}</div>
            <ScoreTable players={[winner, loser]} score={score} />*/}
        </div>
    );
}

export default About;