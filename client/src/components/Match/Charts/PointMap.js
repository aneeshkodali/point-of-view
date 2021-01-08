import React, { useState } from 'react';
import { VictoryChart, VictoryBar, VictoryLine, VictoryLabel } from 'victory';

const PointMap = ({ matchData }) => {

    const { sets, points } = matchData;


    // state for players selected
    const players = matchData['players'];
    const [playerSelected, setPlayerSelected] = useState(players[0]);

    // dropdown options for players
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

    // get chart data ready
    const playerData = [];
    const opponentData = [];

    pointsFiltered.forEach(point => {

        const { point_number, num_shots, server, winner } = point;

        // create necessary columns
        //point['serverRallyCount'] = num_shots === 0 ? 1 : Math.ceil((num_shots+1)/2);
        //point['receiverRallyCount'] = num_shots + 1 - point['serverRallyCount'];
        const serverRallyCount = Math.ceil((num_shots+1)/2);
        const receiverRallyCount = num_shots - serverRallyCount;

        // create columns dependent on player selected
        // multiply by -1 if not player selected
        const playerRallyCount = server['full_name'] === playerSelected['full_name'] ? serverRallyCount : receiverRallyCount;
        const opponentRallyCount = (server['full_name'] === playerSelected['full_name'] ? receiverRallyCount : serverRallyCount)*-1;

        // color bars
        const playerWin = winner['full_name'] === playerSelected['full_name'] ? 'green' : 'lightgrey';
        const opponentWin = winner['full_name'] !== playerSelected['full_name'] ? 'red': 'lightgrey';

        // append data
        playerData.push({ 'x': point_number, 'y': playerRallyCount, 'style': playerWin });
        opponentData.push({ 'x': point_number, 'y': opponentRallyCount, 'style': opponentWin });
    });   

    // create charts
    const chartsRendered =  [playerData, opponentData].map((data, index) => {
        return (
            <VictoryBar key={index}
                data={data}
                alignment="start"
                animate={{
                    duration: 500,
                    onLoad: { duration: 1000 }
                  }}
                style={{
                    data: {
                        fill: ({ datum }) => datum.style
                    }
                }}
            />
        );
    });

    // upper limit for y axis
    const yMax = Math.ceil( Math.max(...pointsFiltered.map(point => point['num_shots']))/2) + 2;

    // create vertical lines for games
    const newGameLines = pointsFiltered.filter(point => point['point_score'] === '0-0').map(point => {
        const { point_number, server, game_score } = point;

        // create label
        const serverInitial = server['full_name'].split(' ').map(name => name[0].toUpperCase()).join('');
        const label = `${serverInitial}\n${game_score}`;

        // create data for chart
        const data = [
            {'x': point_number, 'y': yMax*-1},
            {'x': point_number, 'y': yMax}
        ];
        return (
            <VictoryLine key={point_number}
                data={data}
                style={{
                    data: { stroke: "black", strokeDasharray: [0, 1, 2] },
                  }}
                labels={() => label}
            />
        )
    })

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
                    <VictoryChart>
                        {chartsRendered}
                        {newGameLines}
                    </VictoryChart>
                </div>
            </div>
        </div>
    );
}

export default PointMap;