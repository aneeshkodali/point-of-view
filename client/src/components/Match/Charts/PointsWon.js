import React from 'react';
import { VictoryPie } from 'victory';

const PointsWon = ({ matchData }) => {
    return (
        <div>
            <VictoryPie
                data={[
                    { x: "Cats", y: 35 },
                    { x: "Dogs", y: 40 },
                    { x: "Birds", y: 55 }
                ]}
                />
        </div>
    );
}

export default PointsWon;