import React from 'react';
import { createPointOutcomeData, createPointOutcomeGraph } from './functions';

const Game = ({ data }) => {

    // store text to display
    const textToDisplay = "To start, simply count the number of times you and your opponent end the point a certain way.";

    // create table of point results
    const pointOutcomesData = createPointOutcomeData(data);

    // create graph
    const pointOutcomesGraph = createPointOutcomeGraph(data);



    return (
        <div>
            {textToDisplay}
            {pointOutcomesGraph}
        </div>
    );
}

export default Game;