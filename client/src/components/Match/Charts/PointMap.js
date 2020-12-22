import React, { useState } from 'react';

const PointMap = ({ matchData }) => {

    const { sets } = matchData;

    // state for players selected
    const players = matchData['players'].sort();
    const [playerSelected, setPlayerSelected] = useState(players[0]);

    // dropdown options for players
    const playerOptions = players.map(player => {
        const playerID = player['_id']['$oid'];
        const { full_name } = player;
        const checkedValue = full_name === playerSelected['full_name'] ? 'checked' : ''
        return (
            <div key={playerID} className="field">
                <div className="ui radio checkbox">
                    <input type="radio" name="player" value={player} checked={checkedValue} onClick={() => setPlayerSelected(player)} />
                    <label>{full_name}</label>
                </div>
            </div>
        );
    });

    // state for set selected
    const setNums = Array.from({length: sets}, (_, i) => i+1);
    const [setNumSelected, setSetNumSelected] = useState(setNums[0]);

    // dropdown options for set selected
    const setNumOptions = setNums.map(setNum => {
        const checkedValue = setNum === setNumSelected ? 'checked' : ''
        return (
                <div key={setNum} className="field">
                    <div className="ui radio checkbox">
                        <input type="radio" name="set" value={setNum} checked={checkedValue} onClick={() => setSetNumSelected(setNum)} />
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
                <div>

                </div>
            </div>
        </div>
    )

   
    //return (
    //    <div>
    //        <div>
    //            Player:
    //            <select 
    //                className="ui dropdown"
    //                value={playerSelected} 
    //                onChange={(e) => setPlayerSelected(e.target.value)}
    //            >{playerOptions}
    //            </select>
    //            Set:
    //            <select 
    //                className="ui dropdown"
    //                value={setNumSelected} 
    //                onChange={(e) => setSetNumSelected(e.target.value)}
    //            >{setNumOptions}
    //            </select>
    //        </div>
    //    </div>
    //);
}

export default PointMap;