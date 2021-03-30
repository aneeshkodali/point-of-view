import React, { useState, useEffect } from 'react';

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

    return (
        <div>
            {playerData['full_name']}
        </div>
    )
}

export default Player;