import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import server from '../../api/server';

const Matches = () => {

    // state for matches
    const [matches, setMatches] = useState([])

    // function to get list of matches
    const getMatches = async () => {
        const response = await server.get('/server/matches');
        const matches_db = response['data']['matches']
        setMatches(matches_db)
    }



    const matchesRendered = matches.map(match => {
        const { _id, title } = match
        const id = _id['$oid']
        return (
            <div key={id}>
                <Link to={`/matches/${id}`}>{title}</Link>
            </div>
        );
    });

    return (
        <div>
            <h1>Matches Page</h1>
            <button onClick={getMatches}>Get Matches</button>
            {matchesRendered}
        </div>
    );
}

export default Matches;