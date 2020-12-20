import React, { useState, useEffect } from 'react';

import server from '../../api/server';
import About from './About/About';
import Table from './Data/Table';
import Loader from '../Loader';

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
           const tournament_id = match_data['tournament']['$oid'];
           const tournament_response = await server.get(`/server/tournament/${tournament_id}`);
           const tournament_data = tournament_response.data;
           match_data['tournament'] = tournament_data;

           const player_one_id = match_data['players'][0]['$oid'];
           const player_one_response = await server.get(`/server/player/${player_one_id}`);
           match_data['players'][0] = player_one_response.data;

           const player_two_id = match_data['players'][1]['$oid'];
           const player_two_response = await server.get(`/server/player/${player_two_id}`);
           match_data['players'][1] = player_two_response.data;
           setMatchData(match_data);
       }
    }

    // get match data on component render
    useEffect(() => {
        getMatchData(match_id);
    }, []);

    // state for tabs
    const tabs = ['About', 'Data'];
    const [tabSelected, setTabSelected] = useState(tabs[0]);

    // display loading icon if match data not found
    if (!(matchData && matchData['tournament'] && matchData['players'])) {
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
                    <Table points={matchData.points} />
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

//const Match = (props) => {

//    // state for match data
//    const [matchData, setMatchData] = useState({});
//    // function to get match data
//    const getMatchData = async match_id => {
//        const match_response = await server.get(`/server/match/${match_id}`);
//        const match_data = match_response.data;
//        if (match_data) {
//            setMatchData(match_data);
//            getTournamentData(match_data['tournament']['$oid']);
//            getPlayersData(match_data['players']);
//        }
//    }
    
//    // state for tournament data
//    const [tournamentData, setTournamentData] = useState({});
//    // function to get tournament data
//    const getTournamentData = async tournament_id => {
//        const tournament_response = await server.get(`/server/tournament/${tournament_id}`);
//        setTournamentData(tournament_response.data);
//    }

//    // state for players data
//    const [playersData, setPlayersData] = useState({});
//    // function to get players data
//    const getPlayersData = players => {
//        const players_data = {};
//        players.forEach(async player => {
//            const id = player['$oid'];
//            const player_response = await server.get(`/server/player/${id}`);
//            const player_data = player_response.data;
//            players_data[id] = player_data;
//        })
//        setPlayersData(players_data);
//    }

    
//    useEffect(() => {
//        const match_id = props.match.params.id;
//        getMatchData(match_id);
//    }, []);


//    // state for tabs
//    const tabs = ['About', 'Data'];
//    const [tabSelected, setTabSelected] = useState(tabs[0]);

//    // render tabs
//    const tabsRendered = tabs.map(tab => {
//        const active = tab === tabSelected ? 'active' : '';
//        return (
//            <div key={tab}
//                className={`${active} item`}
//                style={{'cursor': 'pointer'}}
//                onClick={() => setTabSelected(tab)}
//            >
//                {tab}
//            </div>
//        )
//    });

//    const data = {
//        'match': matchData
//    }

//    // conditionally render tab
//    const tabComponentRendered = (tab) => {
//        switch (tab) {
//            case 'About':
//                return (
//                    <About data={data} />  
//                    //<div>ABOUTA</div>
//                );
//            case 'Data':
//                return (
//                    //<Table points={matchData.match.points} />
//                    <div>DATA</div>
//                );
//            default:
//                return null;
//        }
//    }
    
//    // load component if data is loaded else loader
//    const componentRendered = (matchData) ? tabComponentRendered(tabSelected) : <Loader text={"Loading Match Data..."} />;

//   return (
//       <div>
//           <div className="ui top attached tabular menu">
//                {tabsRendered}
//            </div>
//            {componentRendered}
//        </div>
//   );
//}

export default Match;