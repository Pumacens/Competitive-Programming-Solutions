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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    
    for (const letter of s){
        if (/[aeiou]/.test(letter)){
            console.log(letter);
        }
    }

    for (const letter of s){
        if (/[^aeiou]/.test(letter)){
            console.log(letter);
        }
    }
}



// function vowelsAndConsonants(s) {
//     const vowels = 'aeiou';
//     var consonants = '';
    
//     for(var i = 0; i < s.length; i++) {
//        if (vowels.includes(s[i])) {
//            console.log(s[i]);
//        }
//        else {
//            consonants += s[i] + '\n';
//        }
//     }
    
//     console.log(consonants.trim());
// }


// let vowels = [];
// let consonants = [];

// [...s].map(char =>
// {
//     if ('aeiou'.includes(char))
//         vowels.push(char);
//     else
//         consonants.push(char);
// });

// vowels.map(v => console.log(v));
// consonants.map(c => console.log(c));



// let vows = s.match(/[aeiou]/gi).join('\n');
// let letters = s.match(/[^aeiou]/gi).join('\n');
// console.log(vows +"\n"+letters);



// function vowelsAndConsonants(s) {
//     [...s].forEach(c => 'aeiou'.includes(c) ?
//         console.log(c) : null);
//     [...s].forEach(c => 'aeiou'.includes(c) ?
//         null : console.log(c));
// }


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}