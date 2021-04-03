import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import Loader from '../Loader';
import { convertHeight } from '../../helper/functions';
import server from '../../api/server';

const Player = props => {

    // get player_name from link
    const player_name = props.match.params.player_name;

    // state for player data
    const [playerData, setPlayerData] = useState({});

    // function to get player data
    const getPlayerData = async player_name => {
        const player_response = await server.get(`/server/players/${player_name}`);
        const player_data = player_response.data.player;
        setPlayerData(player_data);
       }
    
    // get player data on component render
    useEffect(() => {
        getPlayerData(player_name);
    }, []);


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

    // render player matches
    const matchesRendered = playerData['matches'].map(match => {
        const { match_id, name, suffix } = match
        return (
            <div key={match_id}>
                <Link to={`/players/${player_name}/matches/${suffix}`}>{name}</Link>
            </div>
        );
    });

    // display loading icon if match data not found
    if (Object.keys(playerData).length === 0) {
        return (
            <Loader text={'Loading Player Data...'} />
        );
    }

    return (
        <div>
            {createPlayerCard(playerData)}
            {matchesRendered}
        </div>
    )
}

export default Player;