import React, { useState, useEffect } from 'react';

import server from '../../api/server';
import About from './About/About';
import Game from './Game';
import Loader from '../Loader';
import Table from './Data/Table';
import './Match.css';
//import PointsWon from './Charts/PointsWon';
//import PointMap from './Charts/PointMap';
//import PointsToSet from './Charts/PointsToSet';
//import RallyTree from './Charts/RallyTree';

const Match = props => {

    // get match suffix
    const suffix = props.match.params.suffix;

    // state for match data
    const [data, setData] = useState({});


    // function to get match data
    const getMatchData = async suffix => {
        const match_response = await server.get(`/server/matches/${suffix}`);
        const match_data = match_response.data.match;
        setData(match_data);
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
    if (Object.keys(data).length === 0) {
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
                    <About data={data} />  
                );
            case 'Data':
                return (
                    <Table data={data} />
                );
            case 'Game':
                return (
                    <Game data={data} />
                );
            //case 'Points Won':
            //    return (
            //        <PointsWon data={data} />
            //    );
            //case 'Point Map':
            //    return (
            //        <PointMap data={data} />
            //    );
            //case 'Points to Set':
            //    return (
            //        <PointsToSet data={data} />
            //    );
            //case 'Rally Tree':
            //    return (
            //        <RallyTree data={data} />
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
            <div className='tab-data'>
                {tabComponentRendered(tabSelected)}
            </div>
        </div>
   );

}

export default Match;