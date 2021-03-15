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

    // get points
    const points = [];
    sets.forEach(set => {
        const games = set['games'];
        games.forEach(game => {
            const point_list = game['points']
            point_list.forEach(point => {
                point['winner'] = point['players'].filter(player => player['win'] === 1)[0]['player']
                point['server'] = point['players'].filter(player => player['serve'] === 1)[0]['player']
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
            Click on a point (row) and see details about that point's rally.
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