import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

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
        const id = _id['$oid']
        return <Link key={id} to={`/matches/${id}`}>{title}</Link>
    })

    return (
        <div>
            <h1>Matches Page</h1>
            {matchesRendered}
        </div>
    );
}

export default Matches;