import React from 'react';
import { VictoryPie } from 'victory';

const PointsWon = ({ matchData }) => {

    const { players, points } = matchData;

    // get pie chart data

    // render charts
    const chartsRendered = players.map(player => {

        const player_id = player['_id']['$oid'];
        const point_outcomes = ['ace', 'double fault', 'forced error', 'service winner', 'unforced error', 'winner'];
        const player_data = [];
        point_outcomes.forEach(outcome => {
            const outcome_obj={};
            outcome_obj['x'] = outcome;
            outcome_obj['y'] = matchData.points.filter(point => (point['winner']['_id']['$oid'] === player_id) && (point['result'] === outcome)).length
            player_data.push(outcome_obj);
        });
        return (
            <div className="eight wide column" key={player_id}>
                <VictoryPie
                    data={player_data}
                    colorScale={['tomato', 'orange', 'gold', 'cyan', 'navy', 'pink']}
                    labels={({datum}) => `${datum.x}:${datum.y}`}
                    />
            </div>
        );
    })

    return (
        <div>
            <div className="ui grid">
                {chartsRendered}
            </div>
        </div>
    );
}

export default PointsWon;