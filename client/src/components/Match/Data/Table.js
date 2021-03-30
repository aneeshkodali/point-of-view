import React, { useState } from 'react';

import PointTable from './PointTable';
import Set from '../Helper/Set';
import ShotTable from './ShotTable';

const Table = ({ matchData }) => {

    // get sets as options
    let sets = matchData['sets']
    const setsInMatch = sets.map(set => set['set_in_match'])
    const { setNumSelected, setNumOptions } = Set(setsInMatch, true)

    // potentially filter sets based on setSelected
    sets = setNumSelected === 'All' ? sets : sets.filter(set => set['set_in_match'] === setNumSelected)

     // function to determine score text to display (based on set selected)
     const scoreText = () => {
        if (setNumSelected === 'All') {

            const { players } = matchData;
            return `${players[0]['full_name']} d. ${players[1]['full_name']} ${players[0]['score']}`;

        } else {

            const setSelected = sets[0];
            const { players } = setSelected['games'][setSelected['games'].length-1];
            
            return `${players[0]['full_name']} d. ${players[1]['full_name']} ${players[0]['score']+1}-${players[1]['score']}`
        }
    }


    // get points
    const points = [];
    sets.forEach(set => {
        const games = set['games'];
        games.forEach(game => {
            const point_list = game['points']
            point_list.forEach(point => {

                const server = point['players'].filter(player => player['serve'] === 1)[0]['full_name']

                // get set score
                const serverSetScore = set['players'].filter(player => player['full_name'] === server)[0]['score']
                const receiverSetScore = set['players'].filter(player => player['full_name'] !== server)[0]['score']
                const setScore = `${serverSetScore}-${receiverSetScore}`;
                point['set_score'] = setScore;

                // get game score
                const serverGameScore = game['players'].filter(player => player['full_name'] === server)[0]['score']
                const receiverGameScore = game['players'].filter(player => player['full_name'] !== server)[0]['score']
                const gameScore = `${serverGameScore}-${receiverGameScore}`;
                point['game_score'] = gameScore;

                // get point score
                const serverPointScore = point['players'].filter(player => player['full_name'] === server)[0]['score']
                const receiverPointScore = point['players'].filter(player => player['full_name'] !== server)[0]['score']
                const pointScore = `${serverPointScore}-${receiverPointScore}`;
                point['point_score'] = pointScore;

                point['winner'] = point['players'].filter(player => player['win'] === 1)[0]['full_name']
                point['server'] = server
                point['game_in_match'] = game['game_in_match']
                point['set_in_match'] = set['set_in_match']
                points.push(point)
            })
        })
    })


    // state for currently selected point
    const [pointSelected, setPointSelected] = useState({})
    // state for currently selected shot array
    const [shotsSelected, setShotsSelected] = useState([])

    // function to select point and shots 
    const selectPoint = (point, pointSelected) => {
        // if point is already selected point, deleselect it
        // otherwise select it
        if (point['point_in_match'] === pointSelected['point_in_match']) {
            setPointSelected({})
            setShotsSelected([])
        } else {
            setPointSelected(point)
            setShotsSelected(point['shots'])
        }
    }

   

    return (
        <div>
            <div className="ui form">
                <div className="inline fields">
                    <label>Set</label>
                    {setNumOptions}
                </div>
            </div>
            <div>
                {scoreText()}
            </div>
            <div>
                <div>
                    Click on a point (row) and see details about that point's rally in the Shot Table.
                </div>
                <div>
                    The coloring of certain groups of points helps distinguish one game from another.
                </div>
            </div>
            <div>
                <strong>Note: </strong>Rally Length in the Point Table denotes either (number of shots denotes how many times the ball was touched by a player):
                <ol>
                    <li>
                        number of shots if the point ended via ace, service winner, or winner
                    </li>
                    <li>
                        number of shots - 1 if the point ended via double fault, forced error, or unforced error
                    </li>
                </ol>
            </div>
            <div>
                The Shot Table denotes how many times the ball was touched by a player. For example, if a player double faults (meaning a Rally Length of 0), there will be two shots in the Shot Table (one for each serve attempt).
            </div>
            <div>
                <strong>Note: </strong>The Shot Number w/Serve denotes how many times a player touches a ball. The Shot Number is similar, except, in the event that a player misses a first serve attempt and must hit a second serve, it groups both serves as Shot Number with value of 1. So
                <ul>
                    <li>if a player makes a first serve, Shot Number and Shot Number w/Serve will be identical</li>
                    <li>if a player misses a first serve, Shot Number and Shot Number w/Serve will differ by 1 after the first serve</li>
                </ul>
            </div>
            <div className="ui grid">
                <div className="eight wide column">
                    <PointTable points={points} pointSelected={pointSelected} selectPoint={selectPoint} />
                </div>
                <div className="eight wide column">
                    <ShotTable shots={shotsSelected} />
                </div>
            </div>
        </div>
    );

}

export default Table;