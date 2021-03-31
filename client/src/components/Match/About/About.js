import React from 'react';

import { convertHeight } from '../../../helper/functions';
import ScoreTable from './ScoreTable';
import './About.css'

const About = ({ data }) => {

    // get variables from match data
    const { name, gender, date, round, score, tournament, players } = data;

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

    // get first player in match name
    const firstPlayerName = name.split(': ')[1].split(' vs')[0];
    const firstPlayer = players.filter(player => player['full_name'] === firstPlayerName)[0]
    const secondPlayer = players.filter(player => player !== firstPlayer)[0];

   
    return (
        <div className='container'>
            <div>
                {createPlayerCard(firstPlayer)}
            </div>
            <div>
                <h3>{name}</h3>
                <ScoreTable data={data} />
            </div>
            <div>
                {createPlayerCard(secondPlayer)}
            </div>
        </div>
    );
}

export default About;