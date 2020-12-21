import React, { useState, useEffect } from 'react';

import server from '../../api/server';
import { getPlayerData } from '../../helper/functions';
import About from './About/About';
import Table from './Data/Table';
import Loader from '../Loader';
import PointsWon from './Charts/PointsWon';
import PointsToMap from './Charts/PointsToMap';

const Match = props => {

    // get match id
    const match_id = props.match.params.id;

    // state for match data
    const [matchData, setMatchData] = useState({});


    // function to get match data
    const getMatchData = async match_id => {
       const match_response = await server.get(`/server/match/${match_id}`);
       const match_data = match_response.data;
       if (match_data) {
        
        // get tournament data
        const tournament_id = match_data['tournament']['$oid'];
        const tournament_response = await server.get(`/server/tournament/${tournament_id}`);
        const tournament_data = tournament_response.data;
        match_data['tournament'] = tournament_data;

        // get players data
        const player_one_id = match_data['players'][0]['$oid'];
        const player_one_response = await server.get(`/server/player/${player_one_id}`);
        match_data['players'][0] = player_one_response.data;

        const player_two_id = match_data['players'][1]['$oid'];
        const player_two_response = await server.get(`/server/player/${player_two_id}`);
        match_data['players'][1] = player_two_response.data;

        // add data to match winner/loser
        ['winner', 'loser'].forEach(column => {
            match_data[column] = getPlayerData(match_data[column], match_data['players']);
        });

        // add player data to points/shots
        match_data['points'] = match_data['points'].map(point => {
            // loop through columns in points
            const point_columns = ['server', 'receiver', 'winner' ,'loser'];
            point_columns.forEach(point_column => {
                point[point_column] = getPlayerData(point[point_column], match_data['players']) 
            });
            
            point['shots'] = point['shots'].map(shot_elem => {
                // loop through columns in shots
                const shot_columns = ['shot_by'];
                shot_columns.forEach(shot_column => {
                    shot_elem[shot_column] = getPlayerData(shot_elem[shot_column], match_data['players']);
                });
                return shot_elem;
            });
            
            return point;
        })

        setMatchData(match_data);
       }
    }

    // get match data on component render
    useEffect(() => {
        getMatchData(match_id);
    }, []);

    // state for tabs
    const tabs = ['About', 'Data', 'Points Won', 'Points2Map'];
    const [tabSelected, setTabSelected] = useState(tabs[0]);

    // display loading icon if match data not found
    if (!(matchData && matchData['tournament'] && matchData['players'] && matchData['points'])) {
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
            case 'Points Won':
                return (
                    <PointsWon matchData={matchData} />
                );
            case 'Points2Map':
                return (
                    <PointsToMap matchData={matchData} />
                );
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