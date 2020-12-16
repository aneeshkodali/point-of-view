import React, { useState, useEffect } from 'react';
import server from '../../api/server';

import MatchHeader from './MatchHeader';
import PointTable from './Data/PointTable';

const Match = (props) => {

    // state for match data
    const [matchData, setMatchData] = useState({})

    // get match id from props
    const { id } = props.match.params

    // load match data
    const getMatchData = async id => {
        const response = await server.get(`/server/match/${id}`)
        setMatchData(response.data)
    }
    useEffect(() => {
        getMatchData(id)
    }, [])

    const { title, result, points } = matchData;

    const pointTableRendered = points ? <PointTable points={points} /> : <div>No Points</div>;


   return (
       <div>
           <h1 className="ui header">{title}</h1>
           <h2 className="ui header">{result}</h2>

           <MatchHeader />

           {pointTableRendered}
        </div>
   );
}

export default Match;