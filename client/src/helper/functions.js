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
