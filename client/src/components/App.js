import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Header from './Header';
import Home from './Home';
import Match from './Match/Match';
import Matches from './Match/Matches';
import Player from './Player/Player';
import Players from './Player/Players'

const App = () => {
    return (
        <div>
            <BrowserRouter>
                <Header />
                <Switch>
                    <Route path='/' exact component={Home} />
                    <Route path='/matches' exact component={Matches} />
                    <Route path='/matches/:suffix' component={Match} />
                    <Route path='/players' exact component={Players} />
                    <Route path='/players/:player_name' component={Player} />
                </Switch>
            </BrowserRouter>
        </div>
    )
}

export default App;