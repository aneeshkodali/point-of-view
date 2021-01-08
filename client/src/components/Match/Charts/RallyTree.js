import React, { useState } from 'react';

import { pointOutcomes, createArrayOneToN } from '../../../helper/functions';
import Side from '../Helper/Side';
import Player from '../Helper/Player';
import Set from '../Helper/Set';

const RallyTree = ({ matchData }) => {

    const { sets, points, players } = matchData;

    // get variables from helper components
    const { sideSelected, sideOptions } = Side();
    const { playerSelected, playerOptions } = Player(players);
    const { setNumSelected, setNumOptions } = Set(sets, true);
    
    // filter points data
    let pointsFiltered = points;
    if (sideSelected !== 'All') {
        pointsFiltered = pointsFiltered.filter(({ side }) => side === sideSelected);
    }
    if (setNumSelected !== 'All') {
        pointsFiltered = pointsFiltered.filter(({ set_in_match }) => set_in_match === setNumSelected);
    }


    // CALCULATE DATA

    // get max rally length (CHANGE THIS LATER)
    const maxRallyLength = Math.max(...pointsFiltered.map(({ num_shots }) => num_shots));
    // loop through each rally length
    const rallyLengthArr = createArrayOneToN(maxRallyLength);
    const pointsData = rallyLengthArr.map(rallyLength => {
        // initialize object
        const rallyObj = {};
        rallyObj['rallyLength'] = rallyLength;
        // filter data by rally length
        const pointsRally = pointsFiltered.filter(({ num_shots }) => num_shots === rallyLength);

        // loop through point outcomes and determine points won
        const winObj = {}
        pointOutcomes.forEach(outcome => {
            winObj[outcome] = pointsRally.filter(point => (point['winner']['full_name'] === playerSelected['full_name']) && (point['result'] === outcome)).length;
        });
        // add to object
        rallyObj['win'] = winObj;

        // loop through point outcomes and determine points lost
        const loseObj = {}
        pointOutcomes.forEach(outcome => {
            loseObj[outcome] = pointsRally.filter(point => (point['winner']['full_name'] !== playerSelected['full_name']) && (point['result'] === outcome)).length;
        });
        // add to object
        rallyObj['lose'] = loseObj;

        return rallyObj;

    });
    
    console.log(pointsData);


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