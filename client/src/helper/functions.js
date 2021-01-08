// function to return player data given a player reference
export const getPlayerData = (player, playerArr) => {
    return playerArr.filter(p => p['_id']['$oid'] === player['$oid'])[0];
}

// function to convert date from epoch (in ms) to date string 'yyyy-mm-dd'
export const convertDate = dateEpoch => {
    //get date object
    const dateNew = new Date(0)
    dateNew.setUTCSeconds(dateEpoch['$date']/1000);
    // create date string
    const dateYear = dateNew.getFullYear();
    const month = dateNew.getMonth()+1;
    const dateMonth = month < 10 ? `0${month}` : month;
    const day = dateNew.getDate()+1;
    const dateDay = day < 10 ? `0${day}` : day;
    const dateString = `${dateYear}-${dateMonth}-${dateDay}`;

    return dateString;
}

// function to convert height (cm) to feet
export const convertHeight = heightCM => {
    const inches = Math.floor(heightCM * 0.393701);
    const feet = Math.floor(inches / 12);
    const remainder = inches % 12;
    return `${feet}'${remainder}"`;
}

// function to create an array from 1 to N
export const createArrayOneToN = n => {
    return Array.from({length: n}, (_, i) => i+1);
}

// array of point outcomes
export const pointOutcomes = ['ace', 'double fault', 'forced error', 'service winner', 'unforced error', 'winner'];