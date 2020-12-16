import React, { useState } from 'react';

const PointTable = ({ points }) => {

    // state for currently selected point
    const [pointSelected, setPointSelected] = useState({})

    // function to select point
    const selectPoint = point => {
        // if point is already selected point, deleselect it
        // otherwise select it
        if (point.point_number === pointSelected.point_number) {
            setPointSelected({})
        } else {
            setPointSelected(point)
        }
    }

    const pointsRendered = points.map(point => {
        const { point_number, set_score, game_score, point_score, side, server, rally_length, result, shots } = point
        return (
            <tr key={point_number} onClick={() => selectPoint(point)}>
                <td>{point_number}</td>
                <td>{set_score}</td>
                <td>{game_score}</td>
                <td>{point_score}</td>
                <td>{side}</td>
                {/*<td>{server}</td>*/}
                <td>{rally_length}</td>
                <td>{result}</td>
            </tr>
        )
    })
    return (
        <div>
            Point # Selected: {pointSelected.point_number}
            <table className="ui table">
                <thead>
                    <tr>
                        <th>Point Number</th>
                        <th>Set Score</th>
                        <th>Game Score</th>
                        <th>Point Score</th>
                        <th>Side</th>
                        {/*<th>Server</th>*/}
                        <th>Rally Length</th>
                        <th>Result</th>
                    </tr>
                  
                </thead>
                <tbody>
                    {pointsRendered}
                </tbody>
            </table>
        </div>
    );
}

export default PointTable;