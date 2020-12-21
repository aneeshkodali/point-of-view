import React, { useState } from 'react';

const PointMap = ({ matchData }) => {

    // state for players selected
    const players = matchData['players'].sort();
    const [playerSelected, setPlayerSelected] = useState(players[0]);

    // dropdown options for players
    const playerOptions = players.map(player => {
        const playerID = player['_id']['$oid'];
        const { full_name } = player;
        return (
            <option key={player['_id']['$oid']} value={full_name}>{full_name}</option>
        )
    });

   
    return (
        <div>
            <div>
                Player:
                <select 
                    className="ui dropdown"
                    value={playerSelected} 
                    onChange={(e) => setPlayerSelected(e.target.value)}
                >{playerOptions}
                </select>
            </div>
        </div>
    );
}

export default PointMap;