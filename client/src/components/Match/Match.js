import React, { useState, useEffect } from 'react';
import server from '../../api/server';

import Summary from './Summary';
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

    // state for tabs
    const tabs = ['Summary', 'Data'];
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
            case 'Summary':
                return (
                    <Summary matchData={matchData} />  
                );
            case 'Data':
                return (
                    <PointTable points={matchData['points']} />
                );
            default:
                return null;
        }
    }

   return (
       <div>
           <h1 className="ui header">{matchData['title']}</h1>

           <div className="ui top attached tabular menu">
                {tabsRendered}
            </div>
            {tabComponentRendered(tabSelected)}
        </div>
   );
}

export default Match;