import React, { useState } from 'react';

const Set = sets => {
    // state for set selected
    const setNums = ['All'].concat(Array.from({length: sets}, (_, i) => i+1));
    const [setNumSelected, setSetNumSelected] = useState(setNums[0]);

    // radio options for set selected
    const setNumOptions = setNums.map(setNum => {
        const checkedValue = setNum === setNumSelected ? 'checked' : ''
        return (
                <div key={setNum} className="field">
                    <div className="ui radio checkbox">
                        <input type="radio" name="set" value={setNum} checked={checkedValue} onChange={() => setSetNumSelected(setNum)} />
                        <label>{setNum}</label>
                    </div>
                </div>
            );
    });

    return {
        setNums,
        setNumSelected,
        setSetNumSelected,
        setNumOptions
    }
}

export default Set;