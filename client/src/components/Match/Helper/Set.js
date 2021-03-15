import React, { useState } from 'react';


const Set = (sets, useAll) => {
    // state for set selected
    const setNums = useAll ? ['All'].concat(sets) : sets;
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