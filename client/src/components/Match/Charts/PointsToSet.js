import React, { useState } from 'react';
import { VictoryChart, VictoryLine } from 'victory';

const PointsToSet = ({ matchData }) => {

    const { sets, players, points } = matchData;

    // state for set selected
    const setNums = Array.from({length: sets}, (_, i) => i+1);
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

    // colors for line chart
    const colors = ['blue', 'red'];

    // get chart data - loop through each player to create line
    const chartsRendered = players.map((player, index) => {
        const { full_name } = player;

         // initialize running total value
        let runningTotal = 0;

        // initialize array to store running total
        const runningTotalArray = [];

        // create data array
        const playerData = points.filter(point => point['set_in_match'] === setNumSelected).map((point, index) => {
            const { point_number, winner, game_in_set } = point;

            // get last point in current game
            const lastPointInCurrentGame = Math.max(...points.filter(point => point['game_in_set'] === game_in_set).map(point => point['point_number']));
            //console.log(point_number, lastPointInCurrentGame);

            // check if player won point
            const winPoint = winner.full_name === full_name ? 1 : 0;
            // add to running total
            runningTotal += winPoint;

            return { 'x': point_number, 'y': runningTotal, 'style': colors[index] }
        });
    
        // draw chart
        return (
            <VictoryLine
                data={playerData}
                style={{
                    data: { stroke: colors[index]}
                }}
            />
        );
    
    });

    return (
        <div>
            Keeps a running total of points won by both players with one exception: if a player loses a game, all points won by that player in that game are lost and the total reverts back to the total at the end of the previous game.
            <div className="ui form">
                <div className="inline fields">
                    <label>Set</label>
                    {setNumOptions}
                </div>
            </div>
            <div>
                <VictoryChart>
                    {chartsRendered}
                </VictoryChart>
            </div>
        </div>
    );
}

export default PointsToSet;