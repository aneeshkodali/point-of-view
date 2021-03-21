import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Header from './Header';
import Home from './Home';
import Matches from './Match/Matches';
import Match from './Match/Match';
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
                </Switch>
            </BrowserRouter>
        </div>
    )
}

export default App;