import React, { useState } from 'react';

import PointTable from './PointTable';

const Table = ({ points }) => {

    // state for currently selected point
    const [pointSelected, setPointSelected] = useState({})
    // state for currently selected shot array
    const [shotsSelected, setShotsSelected] = useState([])

    // function to select point and shots 
    const selectPoint = (point, pointSelected) => {
        // if point is already selected point, deleselect it
        // otherwise select it
        if (point.point_number === pointSelected.point_number) {
            setPointSelected({})
            setShotsSelected([])
        } else {
            setPointSelected(point)
            setShotsSelected(point.shots)
        }
    }

    return (
            <div className="ui grid">
                <div className="eight wide column">
                    <PointTable points={points} pointSelected={pointSelected} selectPoint={selectPoint} />
                </div>
                <div className="eight wide column">
                    SHOT TABLE
                </div>
            </div>
    );
}

export default Table;