import { VictoryChart, VictoryGroup, VictoryBar, VictoryLabel } from 'victory';

const results = ['ace', 'double fault', 'forced error', 'service winner', 'unforced error', 'winner'];

export const createPointOutcomeData = (matchData) => {

    // get players
    const players = matchData['players'].map(player => player['full_name']);

    // create initial array of objects
    const pointResults = [];

    // loop through players and results to create objects
    players.forEach(player => {
        results.forEach(result => {
            let resultObj = {};
            resultObj['player'] = player;
            resultObj['result'] = result;
            resultObj['count'] = 0;
            pointResults.push(resultObj);
        });
    });

    // loop through matchData and update counts
    matchData['sets'].forEach(set => {
        set['games'].forEach(game => {
            game['points'].forEach(point => {               
                point['shots'].forEach(shot => {
                    const { result, shot_by } = shot;
                    if (results.includes(result)) {
                        pointResults.filter(resultObj => (resultObj['player'] === shot_by) && (resultObj['result'] === result))[0]['count'] ++;
                    }
                });
            });
        });
    });

    // return
    return pointResults;
}


export const createPointOutcomeGraph = matchData => {

    // create point outcomes table
    const pointOutcomesData = createPointOutcomeData(matchData);

    // create array of VictoryBar
    const players = [...new Set(pointOutcomesData.map(obj => obj['player']))]
    const playerVictoryBars = players.map(player => {
        // filter pointOutcomesData to just player objects and add x and y values
        const pointOutcomesPlayer = pointOutcomesData.filter(obj => obj['player'] === player).map(obj => {
            obj['x'] = obj['result'];
            obj['y'] = obj['count'];
            return obj;
        });
        return (
            <VictoryBar
                data={pointOutcomesPlayer}
            />
        )
    })

    return (
        <div>
          <VictoryChart
          >
              <VictoryGroup
                offset={15}
                style={{ data: { width: 10 } }}
                categories={{x:results}}

              >
                {playerVictoryBars}
            </VictoryGroup>
          </VictoryChart>
        </div>
      );
}