import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Header from './Header';
import Matches from './Match/Matches';
import Players from './Player/Players'

const App = () => {
    return (
        <div>
            <BrowserRouter>
                <Header />
                <Switch>
                    <Route path='/matches' exact component={Matches} />
                    <Route path='/players' exact component={Players} />
                </Switch>
            </BrowserRouter>

        WELCOME TO MY APP
        </div>
    )
}

export default App;