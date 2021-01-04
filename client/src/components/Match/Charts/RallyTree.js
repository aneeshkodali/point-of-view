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
    
    // filter points data
    let pointsFiltered = points;
    if (sideSelected !== 'All') {
        pointsFiltered = pointsFiltered.filter(({ side }) => side === sideSelected);
    }
    if (setNumSelected !== 'All') {
        pointsFiltered = pointsFiltered.filter(({ set_in_match }) => set_in_match === setNumSelected);
    }

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
            <div>
                {pointsFiltered.length}
            </div>
        </div>
    );
}

export default RallyTree;