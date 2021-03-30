import React, { useState, useEffect } from 'react';

import server from '../../api/server';
import About from './About/About';
import Game from './Game';
import Loader from '../Loader';
import Table from './Data/Table';
//import PointsWon from './Charts/PointsWon';
//import PointMap from './Charts/PointMap';
//import PointsToSet from './Charts/PointsToSet';
//import RallyTree from './Charts/RallyTree';

const Match = props => {

    // get match suffix
    const suffix = props.match.params.suffix;

    // state for match data
    const [matchData, setMatchData] = useState({});


    // function to get match data
    const getMatchData = async suffix => {
        const match_response = await server.get(`/server/matches/${suffix}`);
        const match_data = match_response.data.match;
        setMatchData(match_data);
       }
    

    // get match data on component render
    useEffect(() => {
        getMatchData(suffix);
    }, []);

    // state for tabs
    //const tabs = ['About', 'Data', 'Points Won', 'Point Map', 'Points to Set', 'Rally Tree'];
    const tabs = ['About', 'Game', 'Point', 'Shot'];
    const [tabSelected, setTabSelected] = useState(tabs[0]);

    // display loading icon if match data not found
    if (Object.keys(matchData).length === 0) {
        return (
            <Loader text={'Loading Match Data...'} />
        );
    }

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
                    <Table matchData={matchData} />
                );
            case 'Game':
                return (
                    <Game data={matchData} />
                );
            //case 'Points Won':
            //    return (
            //        <PointsWon matchData={matchData} />
            //    );
            //case 'Point Map':
            //    return (
            //        <PointMap matchData={matchData} />
            //    );
            //case 'Points to Set':
            //    return (
            //        <PointsToSet matchData={matchData} />
            //    );
            //case 'Rally Tree':
            //    return (
            //        <RallyTree matchData={matchData} />
            //    );
            default:
                return null;
        }
    }

      return (
       <div>
           <div className="ui top attached tabular menu">
                {tabsRendered}
            </div>
            {tabComponentRendered(tabSelected)}
        </div>
   );

}

export default Match;