import React from 'react';

import { convertHeight } from '../../../helper/functions';
import ScoreTable from './ScoreTable';

const About = ({ matchData }) => {

    // get variables from match data
    const { name, gender, date, round, score, tournament, players } = matchData;

    // function to create player card
    const createPlayerCard = player => {
        const { player_id, full_name, image_url, country, backhand, date_of_birth, hand, height } = player;
        return (
            <div key={player_id} className="ui card">
                <div className="content">
                    <div className="center aligned header">{full_name} ({country})</div>
                </div>
                <div>
                    <img className="ui centered image" src={image_url} alt={full_name} />
                </div>
                <div className="content">
                    <div className="description">
                        <span className="right floated">Height: {convertHeight(height)}</span>
                        Born: {date_of_birth}
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
            <div><span style={{fontWeight:"bold"}}>Tournament</span>: {tournament['tournament_name']}</div>
            <div><span style={{fontWeight:"bold"}}>Round</span>: {round}</div>
            <div><span style={{fontWeight:"bold"}}>Date</span>: {date}</div>
        </div>
    );

   
    return (
        <div>
            <div className="ui equal width grid">
                    <div className="column">{createPlayerCard(players[0])}</div>
                    <div className="column">
                        {matchInfo}
                        <ScoreTable matchData={matchData} />
                    </div>
                    <div className="column">{createPlayerCard(players[1])}</div>
            </div>
        </div>
    );
}

export default About;