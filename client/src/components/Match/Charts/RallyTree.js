import React, { useState } from 'react';

const RallyTree = ({ matchData }) => {

    const { sets, points } = matchData;

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

    // state for set selected
    const setNums = ['All'].concat(Array.from({length: sets}, (_, i) => i+1));
    const [setNumSelected, setSetNumSelected] = useState(setNums[0]);

    // dropdown options for set selected
    const setNumOptions = setNums.map(setNum => {
        const checkedValue = setNum === setNumSelected ? 'checked' : ''
        return (
                <div key={setNum} className="field">
                    <div className="ui radio checkbox">
                        <input type="radio" name="set" value={setNum} checked={checkedValue} onChange={() => setSetNumSelected(setNum)} />
                        <label>{setNum}</label>
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
                <div className="inline fields">
                    <label>Set</label>
                    {setNumOptions}
                </div>
            </div>
        </div>
    );
}

export default RallyTree;