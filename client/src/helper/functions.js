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