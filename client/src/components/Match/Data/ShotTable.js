import React from 'react';


const ShotTable = ({ shots }) => {


    // display shots
    const shotsRendered = shots.map(shot_elem => {
        const { shot_number, shot_number_w_serve, shot_by, shot, location, result } = shot_elem
        return (
            <tr key={shot_number_w_serve}>
                <td>{shot_number}</td>
                <td>{shot_number_w_serve}</td>
                <td>{shot_by}</td>
                <td>{shot}</td>
                <td>{location}</td>
                <td>{result}</td>
            </tr>
        );
    })

    return (
        <div>
            <h1 className="ui header">Shot Table</h1>
            <br></br>
            <table className="ui celled table">
                <thead>
                    <tr>
                        <th>Shot Number</th>
                        <th>Shot Number w/Serve</th>
                        <th>Shot By</th>
                        <th>Shot</th>
                        <th>Location</th>
                        <th>Result</th>
                    </tr>
                </thead>
                <tbody>
                    {shotsRendered}
                </tbody>
            </table>
        </div>
    );
}

export default ShotTable;