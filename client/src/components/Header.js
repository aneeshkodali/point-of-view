import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <div className="ui secondary menu">
            <Link to='/' className="item">
                Home
            </Link>
            <Link to='/matches' className="item">
                Matches
            </Link>
            <Link to='/players' className="item">
                Players
            </Link>
        </div>
    );
};

export default Header;