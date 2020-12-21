import React from 'react';


const PointTable = ({ points, pointSelected, selectPoint }) => {


    // display points
    const pointsRendered = points.map(point => {
        const { point_number, set_score, game_score, point_score, side, server, rally_length, result, shots } = point
        return (
            <tr key={point_number} onClick={() => selectPoint(point, pointSelected)}>
                <td>{point_number}</td>
                <td>{set_score}</td>
                <td>{game_score}</td>
                <td>{point_score}</td>
                <td>{side}</td>
                <td>{server.full_name}</td>
                <td>{rally_length}</td>
                <td>{result}</td>
            </tr>
        );
    });


    return (
        <div>
            <h1 className="ui header">Point Table</h1>
            Point # Selected: <b>{pointSelected.point_number}</b>
            <table className="ui celled table">
                <thead>
                    <tr>
                        <th>Point Number</th>
                        <th>Set Score</th>
                        <th>Game Score</th>
                        <th>Point Score</th>
                        <th>Side</th>
                        <th>Server</th>
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