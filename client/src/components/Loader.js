import React from 'react';

const Loader = ({ text }) => {
    return (
        <div className="ui segment">
            <div className="ui active inverted inline dimmer">
                <div className="ui text loader">{text}</div>
            </div>
        </div>
    );
}

export default Loader;

