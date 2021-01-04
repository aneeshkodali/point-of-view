import React, { useState } from 'react';

const Player = players => {
    
    // state for player
    const [playerSelected, setPlayerSelected] = useState(players[0]);

    // radio options for players
    const playerOptions = players.map(player => {
        const playerID = player['_id']['$oid'];
        const { full_name } = player;
        const checkedValue = full_name === playerSelected['full_name'] ? 'checked' : ''
        return (
            <div key={playerID} className="field">
                <div className="ui radio checkbox">
                    <input type="radio" name="player" value={player} checked={checkedValue} onChange={() => setPlayerSelected(player)} />
                    <label>{full_name}</label>
                </div>
            </div>
        );
    });

    return {
        playerSelected,
        setPlayerSelected,
        playerOptions
    }
    
}

export default Player;