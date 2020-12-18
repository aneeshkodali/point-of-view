import React, { useState, useEffect } from 'react';
import server from '../../api/server';

import About from './About/About';
import Table from './Data/Table';
import Loader from '../Loader';

const Match = (props) => {

    // state for match data
    const [matchData, setMatchData] = useState({})

    // get match id from props
    const { id } = props.match.params

    // load match data
    const getMatchData = async id => {

        // get match data
        const match_response = await server.get(`/server/match/${id}`);
        const match_data = match_response.data;
        
        // get tournament data
        const tournament_id = match_data['tournament']['$oid'];
        const tournament_response = await server.get(`/server/tournament/${tournament_id}`);
        const tournament_data = tournament_response.data;

        // get player data
        const players_data = {}
        match_data['players'].forEach(async player => {
            const id = player['$oid'];
            const player_response = await server.get(`/server/player/${id}`);
            const player_data = player_response.data
            players_data[id] = player_data
        });

        // combine all data
        const matchDataObj = await {
            'match': match_data,
            'tournament': tournament_data,
            'players': players_data
        }
        setMatchData(matchDataObj)
    }
    useEffect(() => {
        getMatchData(id)
    }, []);


    // state for tabs
    const tabs = ['About', 'Data'];
    const [tabSelected, setTabSelected] = useState(tabs[0]);

    // render tabs
    const tabsRendered = tabs.map(tab => {
        const active = tab === tabSelected ? 'active' : '';
        return (
            <div key={tab}
                className={`${active} item`}
                style={{'cursor': 'pointer'}}
                onClick={() => setTabSelected(tab)}
            >
                {tab}
            </div>
        )
    });

    // conditionally render tab
    const tabComponentRendered = (tab) => {
        switch (tab) {
            case 'About':
                return (
                    <About matchData={matchData} />  
                    //<div>ABOUTA</div>
                );
            case 'Data':
                return (
                    //<Table points={matchData.match.points} />
                    <div>DATA</div>
                );
            default:
                return null;
        }
    }
    
    // load component if data is loaded else loader
    const { match, tournament, players } = matchData;
    const componentRendered = (match && tournament && players) ? tabComponentRendered(tabSelected) : <Loader text={"Loading Match Data..."} />;

   return (
       <div>
           <div className="ui top attached tabular menu">
                {tabsRendered}
            </div>
            {componentRendered}
        </div>
   );
}

export default Match;