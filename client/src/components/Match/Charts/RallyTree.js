import React, { useState } from 'react';

import Side from '../Helper/Side';
import Player from '../Helper/Player';
import Set from '../Helper/Set';

const RallyTree = ({ matchData }) => {

    const { sets, points, players } = matchData;

    // get variables from helper components
    const { sideSelected, sideOptions } = Side();
    const { playerSelected, playerOptions } = Player(players);
    const { setNumSelected, setNumOptions } = Set(sets);
    
 

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