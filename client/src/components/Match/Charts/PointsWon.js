import React, { useState } from 'react';
import { VictoryPie } from 'victory';

const PointsWon = ({ matchData }) => {

    const { players, sets, points } = matchData;

    // state for set selected
    const setNums = ['All'].concat(Array.from({length: sets}, (_, i) => i+1));
    const [setNumSelected, setSetNumSelected] = useState(setNums[0]);

    // create dropdown
    const setNumOptions = setNums.map(setNum => {
        return (
                <option key={setNum} value={setNum}>
                    {setNum}
                </option>
                )
    });

    // render charts - loop through each player
    const chartsRendered = players.map(player => {

        const playerID = player['_id']['$oid'];
        const pointOutcomes = ['ace', 'double fault', 'forced error', 'service winner', 'unforced error', 'winner'];
        const playerData = [];
        let playerSum = 0;
        // for each outcome, count number of points player won and add to data array
        pointOutcomes.forEach(outcome => {
            const outcomeObj = {};
            outcomeObj['x'] = outcome;
            let pointsFiltered = points.filter(point => (point['winner']['_id']['$oid'] === playerID) && (point['result'] === outcome));
            if (setNumSelected !== 'All') {
                pointsFiltered = pointsFiltered.filter(point => point['set_in_match'] === parseInt(setNumSelected, 10));
            }
            outcomeObj['y'] = pointsFiltered.length;
            playerData.push(outcomeObj);
            playerSum += pointsFiltered.length;
        });
        return (
            <div className="eight wide column" key={playerID}>
                <h2 className="ui centered header">{player['full_name']} ({playerSum})</h2>
                <VictoryPie
                    data={playerData}
                    colorScale={['tomato', 'orange', 'gold', 'cyan', 'navy', 'pink']}
                    labels={({datum}) => `${datum.x}:${datum.y}`}
                    />
            </div>
        );
    })

    return (
        <div>
            <div>
                <select 
                    className="ui dropdown"
                    value={setNumSelected}
                    onChange={(e) => setSetNumSelected(e.target.value)}
                >{setNumOptions}</select>
            </div>
            <div className="ui grid">
                {chartsRendered}
            </div>
        </div>
    );
}

export default PointsWon;