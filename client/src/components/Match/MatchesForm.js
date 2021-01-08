import React, { useState, useEffect } from 'react';

import server from '../../api/server';

const MatchesForm = () => {

    // GENDER
    // state for gender dropdown
    const [genderOptions, setGenderOptions] = useState(['All'])
    const [genderOptionSelected, setGenderOptionSelected] = useState(genderOptions[0]);

    const [setOptions, setSetOptions] = useState(['All']);
    const [setOptionSelected, setSetOptionSelected] = useState(setOptions[0]);

    // function to get unique values
    const getUniqueValues = async (field, stateArray, setStateFunction) => {
        const response = await server.get(`/server/matches/unique/${field}`)
        const { values } = response.data
        const updatedArray = [...stateArray, ...values]
        setStateFunction(updatedArray)
    }
    useEffect(() => {
        getUniqueValues('gender', genderOptions, setGenderOptions) 
        getUniqueValues('sets', setOptions, setSetOptions)
    }, []);

    // render options
    const genderOptionsRendered = genderOptions.map(genderOption => {
        return (
                <option 
                    key={genderOption}
                    value={genderOption}
                >
                    {genderOption}
                </option>
                )
    });

    const setOptionsRendered = setOptions.map(setOption => {
        return (
                <option 
                    key={setOption}
                    value={setOption}
                >
                    {setOption}
                </option>
                )
    });

    return (
        <div>
            FORM
            <div className="ui form">
                <div>
                    <select 
                        className="ui dropdown"
                        value={genderOptionSelected}
                        onChange={(e) => setGenderOptionSelected(e.target.value)}
                    >
                        {genderOptionsRendered}
                    </select>
                </div>
                <div>
                    <select 
                        className="ui dropdown"
                        value={setOptionSelected}
                        onChange={(e) => setSetOptionSelected(e.target.value)}
                    >
                        {setOptionsRendered}
                    </select>
                </div>
            </div>
        </div>
    );
}

export default MatchesForm;