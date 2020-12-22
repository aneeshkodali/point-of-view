import React, { useState } from 'react';
import { VictoryBar } from 'victory';

const PointMap = ({ matchData }) => {

    const { sets, points } = matchData;


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

    // filter points
    const pointsFiltered = points.filter(point => point['set_in_match'] === parseInt(setNumSelected, 10));

    // color list for bars
    const colorList=['#FFA04E', '#FFDB3E'];

    const chartsRendered = players.map((player, index) => {

        const player_data = [];

        const points_data = pointsFiltered.map(point => {
            const { point_number, num_shots, server, winner } = point;

            // create necessary columns
            point['serverRallyCount'] = num_shots === 0 ? 1 : Math.ceil((num_shots+1)/2);
            point['receiverRallyCount'] = num_shots + 1 - point['serverRallyCount'];

            // create columns dependent on player selected
            point['playerRallyCount'] = server['full_name'] === playerSelected['full_name'] ? point['serverRallyCount'] : point['receiverRallyCount'];
            point['opponentRallyCount'] = server['full_name'] === playerSelected['full_name'] ? point['receiverRallyCount'] : point['serverRallyCount']*-1;

            
            // color bars
            point['playerWin'] = winner['full_name'] === playerSelected['full_name'] ? colorList[index] : 'lightgrey';

            player_data.push({'x': point_number, 'y': point['playerRallyCount']})
        });

        const chart = (
            <VictoryBar 
                data={player_data}
                //style={points_data.map(point => point['playerWin'])}
            />
        );
        
        return chart;
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
                    {chartsRendered}
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