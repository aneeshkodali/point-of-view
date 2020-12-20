// function to return player data given a player reference
export const getPlayerData = (player, playerArr) => {
    return playerArr.filter(p => p['_id']['$oid'] === player['$oid'])[0];
}
