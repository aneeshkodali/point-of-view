import React from 'react';

const PointTable = ({ points }) => {

    const pointsRendered = points.map(point => {
        const { point_number, set_score, game_score, point_score, side, server, rally_length, result, shots } = point
        return (
            <tr key={point_number}>
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