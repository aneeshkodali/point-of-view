import React from 'react';


const PointTable = ({ points, pointSelected, selectPoint }) => {


    // display points
    const pointsRendered = points.map(point => {
        const { point_in_match, game_in_match, set_in_match, point_score, game_score, set_score, side, rally_length, result, server, winner, shots } = point;

        // highlight row if point is pointSelected
        const rowStyling = point => {
            let backgroundColor;
            if (point['point_in_match'] === pointSelected['point_in_match']) {
                backgroundColor = 'lightgreen';
            } else {
                backgroundColor = point['game_in_match'] % 2 === 0 ? 'lightgray' : '';
            }

            return {
                'cursor': 'pointer',
                'backgroundColor': backgroundColor
            }
        }
        

        return (
            <tr key={point_in_match} onClick={() => selectPoint(point, pointSelected)} style={rowStyling(point)}>
                <td>{point_in_match}</td>
                <td>{set_score}</td>
                <td>{game_score}</td>
                <td>{point_score}</td>
                <td>{side}</td>
                <td>{server}</td>
                <td>{rally_length}</td>
                <td>{result}</td>
                <td>{winner}</td>
            </tr>
        );
    });


    return (
        <div>
            <h1 className="ui header">Point Table</h1>
            Point # Selected: <b>{pointSelected['point_in_match']}</b>
            <table className="ui celled table">
                <thead>
                    <tr>
                        <th>Point #</th>
                        <th>Set</th>
                        <th>Game</th>
                        <th>Point</th>
                        <th>Side</th>
                        <th>Server</th>
                        <th>Rally Length</th>
                        <th>Result</th>
                        <th>Winner</th>
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