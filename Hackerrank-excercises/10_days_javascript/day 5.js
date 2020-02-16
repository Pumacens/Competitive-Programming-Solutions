'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {

    if (25 < score && score <= 30){
        return 'A';

    } else if (20 < score && score <= 25){
        return 'B';

    } else if (15 < score && score <= 20){
        return 'C';

    } else if (10 < score && score <= 15){
        return 'D';

    } else if (5 < score && score <= 10){
        return 'E';

    } else if (0 <= score && score <= 5){
        return 'F';
    }
    
}


// function getGrade(score) {
//     return 'FFEDCBA'[Math.ceil(score/5.0)];
// }


// if(0<=score && score<=30){
//     grade = String.fromCharCode(70 - parseInt((score-1)/5));
// }


function main() {
    const score = +(readLine());
    
    console.log(getGrade(score));
}