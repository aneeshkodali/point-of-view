import React, { useState } from 'react';
import { VictoryChart, VictoryLine, VictoryLegend } from 'victory';

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

    // filter points
    const pointsFiltered = points.filter(point => point['set_in_match'] === parseInt(setNumSelected, 10));


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
        const playerData = pointsFiltered.map((point, pointIndex) => {
            const { point_number, winner, game_in_set } = point;

            // get last point in current game
            const lastPointInCurrentGame = Math.max(...pointsFiltered.filter(point => point['game_in_set'] === game_in_set).map(point => point['point_number']));
            // get index of first point in current game
            const firstPointInCurrentGameIndex = Math.min(...pointsFiltered.filter(point => point['game_in_set'] === game_in_set).map(point => point['point_number']));

            // check if player won point
            const winPoint = winner['full_name'] === full_name ? 1 : 0;
            // add to running total
            runningTotal += winPoint;

            // if player loses point and point is last point in game, revert back to previous end-of-game total
            // otherwise, add to running total as usual
            if (pointIndex === 0) {
                runningTotalArray[0] = winPoint;
            }  else {
                if (!winPoint && (point_number === lastPointInCurrentGame)) {
                    if (game_in_set === 1) {
                        runningTotalArray[pointIndex] = 0;
                    } else {
                        runningTotalArray[pointIndex] = runningTotalArray[firstPointInCurrentGameIndex];
                    }
                } else {
                    runningTotalArray[pointIndex] = runningTotalArray[pointIndex-1] + winPoint;
                }
            }

            return { 'x': point_number, 'y': runningTotalArray[pointIndex], 'style': colors[index] }
        });
    
        console.log(runningTotalArray);
        // draw chart
        return (
            <VictoryLine key={full_name}
                data={playerData}
                style={{
                    data: { stroke: colors[index]}
                }}
            />
        );
    
    });

    // upper limit for y axis
    const yMax = Math.ceil( Math.max(...pointsFiltered.map((point, index) => index))) + 2;

    // create vertical lines for games
    const newGameLines = pointsFiltered.filter(point => point['point_score'] === '0-0').map((point, index) => {
        const { point_number, server, game_score } = point;

        // create label
        const serverInitial = server['full_name'].split(' ').map(name => name[0].toUpperCase()).join('');
        const label = `${serverInitial}\n${game_score}`;

        // create data for chart
        const data = [
            {'x': point_number, 'y': 0},
            {'x': point_number, 'y': yMax}
        ];
        return (
            <VictoryLine key={point_number}
                data={data}
                style={{
                    data: index !== 0 ? { stroke: "black", strokeDasharray: [0, 1, 2] } : {},
                  }}
                labels={({ datum }) => datum.y !== 0 ? label : ''}
            />
        )
    });

    // legend
    const legendData = players.map((player, index) => {
        return { name: player['full_name'], symbol: { fill: colors[index]}}
    });
    const chartLegend = (
        <VictoryLegend
            data={legendData}
        />
    );


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
                    {newGameLines}
                    {chartLegend}
                </VictoryChart>
            </div>
        </div>
    );
}

export default PointsToSet;