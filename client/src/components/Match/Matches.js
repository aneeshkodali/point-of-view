import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import server from '../../api/server';
import MatchesForm from './MatchesForm';

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
        const { match_id, name } = match
        return (
            <div key={match_id}>
                <Link to={`/matches/${match_id}`}>{name}</Link>
            </div>
        );
    });

    return (
        <div>
            <h1>Matches Page</h1>
            {/*<MatchesForm />*/}
            <button onClick={getMatches}>Get Matches</button>
            {matchesRendered}
        </div>
    );
}

export default Matches;