import React, { useState, useEffect } from 'react';

import server from '../../api/server';

const Matches = () => {

    // state for matches
    const [matches, setMatches] = useState([])
    useEffect(() => {
        const getMatches = async () => {
            const response = await server.get('/server/matches');
            const matches_db = response['data']['matches']
            setMatches(matches_db)
        }
        getMatches()
    }, []);


    const matchesRendered = matches.map(match => {
        const { _id, title } = match
        return <li key={_id}>{title}</li>
    })

    return (
        <div>
            <h1>Matches Page</h1>
            {matchesRendered}
        </div>
    );
}

export default Matches;