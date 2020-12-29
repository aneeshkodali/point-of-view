import React, { useState } from 'react';

const RallyTree = ({ matchData }) => {

    // state for player
    const players = matchData['players'];
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


    return (
        <div>
            <div className="ui form">
                <div className="inline fields">
                    <label>Player</label>
                    {playerOptions}
                </div>
            </div>
        </div>
    );
}

export default RallyTree;