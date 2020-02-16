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

function getLetter(s) {
    let letter = s[0];
    
    switch(letter){
        case 'a': case 'e': case 'i': case 'o': case 'u':
            return 'A';
            break;

        case 'b': case 'c': case 'd': case 'f': case 'g':
            return 'B';
            break;

        case 'h': case 'j': case 'k': case 'l': case 'm':
            return 'C';
            break;

        default:
            return 'D';
            break;
    }
    
}


// function getLetter(s) {
//     let letter;
//     // Write your code here
//     switch (true) {
//         case 'aeiou'.includes(s[0]):
//             letter = 'A';
//             break;
//         case 'bcdfg'.includes(s[0]):
//             letter = 'B';
//             break;
//         case 'hjklm'.includes(s[0]):
//             letter = 'C';
//             break;
//         case 'npqrstvwxyz'.includes(s[0]):
//             letter = 'D';
//             break;
//     }
//     return letter;
// }



// function getLetter(s) {
//     let letter;
//     // Write your code here
//     switch (true) {
//         case /^[aeiou]/.test(s):
//             letter = "A";
//             break;
//         case /^[bcdfg]/.test(s):
//             letter = "B";
//             break;
//         case /^[hjklm]/.test(s):
//             letter = "C";
//             break;
//         case /^[npqrstvwxyz]/.test(s):
//             letter = "D";
//             break;
//     }
//     return letter;
// }




// //This was JavaScript with sugar syntax (es6, i guess)

// //vanilla JavaScript
// function getLetter(s) {
//     var firstElement = s[0];
//     var indexInCriteria = 'aeioubcdfghjklm'.indexOf(firstElement);
//     var divisionByFiveOfCriteria = indexInCriteria / 5;
//     // if a~u == 0.x
//     // if b~g == 1.x
//     // if h~m == 2.x
//     // if not in criteria or n~z == -1
  
//     //get a index position
//     //so the options is -1~2.x increment to be 0~3.x and trunc
//     var position = Number.parseInt(divisionByFiveOfCriteria + 1);
//     //0 for not in criteria must return D
//     //1 for a~u must return A
//     //2 for b~g must return B
//     //3 for h~m must return C
//     //I did this order to not write the n~z in the criteria (kinda default)
//     return 'DABC'[position];
//   };


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}