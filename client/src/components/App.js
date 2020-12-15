import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Matches from './Match/Matches';

const App = () => {
    return (
        <div>
            <BrowserRouter>
                HEADER
                <Switch>
                    <Route path='/matches' exact component={Matches} />
                </Switch>
            </BrowserRouter>

        WELCOME TO MY APP
        </div>
    )
}

export default App;