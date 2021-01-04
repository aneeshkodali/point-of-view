import React, { useState } from 'react';

const Side = () => {

    // state for side
    const sides = ['All', 'deuce', 'ad'];
    const [sideSelected, setSideSelected] = useState(sides[0]);

    // radio options for set selected
    const sideOptions = sides.map(side => {
        const checkedValue = side === sideSelected ? 'checked' : ''
        return (
                <div key={side} className="field">
                    <div className="ui radio checkbox">
                        <input type="radio" name="side" value={side} checked={checkedValue} onChange={() => setSideSelected(side)} />
                        <label>{side}</label>
                    </div>
                </div>
            );
    });

    return {
        sides,
        sideSelected,
        setSideSelected,
        sideOptions
    }
}


export default Side;
