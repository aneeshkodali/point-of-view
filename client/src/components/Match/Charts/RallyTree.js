import React, { useState } from 'react';

import Side from '../Helper/Side';
import Player from '../Helper/Player';

const RallyTree = ({ matchData }) => {

    const { sets, points, players } = matchData;

    // get variables from Side helper component
    const { sideSelected, sideOptions } = Side();

    // get varibles from Player helper component
    const { playerSelected, playerOptions } = Player(players)


    // state for set selected
    const setNums = ['All'].concat(Array.from({length: sets}, (_, i) => i+1));
    const [setNumSelected, setSetNumSelected] = useState(setNums[0]);

    // radio options for set selected
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
                <div className="inline fields">
                    <label>Side</label>
                    {sideOptions}
                </div>
            </div>
        </div>
    );
}

export default RallyTree;