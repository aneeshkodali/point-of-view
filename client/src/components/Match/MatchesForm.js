import React, { useState, useEffect } from 'react';

import server from '../../api/server';

const MatchesForm = () => {

    // GENDER
    // state for gender dropdown
    const [genderOptions, setGenderOptions] = useState(['All'])
    const [genderOptionSelected, setGenderOptionSelected] = useState(genderOptions[0]);
    // function to get unique values
    const getUniqueGenderValues = async () => {
        const response = await server.get('/server/matches/unique/gender')
        const { values } = response.data
        const new_arr = [...genderOptions, ...values]
        setGenderOptions(new_arr)
    }
    useEffect(() => {
        getUniqueGenderValues() 
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
            </div>
        </div>
    );
}

export default MatchesForm;