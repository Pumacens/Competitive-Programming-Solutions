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
/*
 * Create the function factorial here
 */

function factorial(n){
    let result = 1;

    for(let i=2; i<=n; i++){
        result *= i;
    }

    return result;
}


// function factorial(n) {
//     return (n > 1) ? n * factorial(n - 1) : 1;
// }


// var factorial = (num) => {
//     for (var i = num - 1; i > 0; i--){
//         num *= i;
//     }
//     return num;
// }


function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}