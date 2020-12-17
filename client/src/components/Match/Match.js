import React, { useState, useEffect } from 'react';
import server from '../../api/server';

import About from './About/About';
import Table from './Data/Table';

const Match = (props) => {

    // state for match data
    const [matchData, setMatchData] = useState({})

    // get match id from props
    const { id } = props.match.params

    // load match data
    const getMatchData = async id => {
        const match_response = await server.get(`/server/match/${id}`);
        const match_data = match_response.data;
        
        // get tournament data
        const tournament_id = match_data['tournament']['$oid'];
        const tournament_response = await server.get(`/server/tournament/${tournament_id}`);
        match_data['tournament'] = tournament_response.data;

        setMatchData(match_data)
    }
    useEffect(() => {
        getMatchData(id)
    }, []);

    // get points data to send to components
    const { points } = matchData

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
                );
            case 'Data':
                return (
                    <Table points={points} />
                );
            default:
                return null;
        }
    }

    // create loader component
    const loader = (
        <div className="ui segment">
            <div className="ui active inverted inline dimmer">
                <div className="ui text loader">Loading Match Data...</div>
            </div>
        </div>
    );

    const componentRendered = points ? tabComponentRendered(tabSelected) : loader;

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