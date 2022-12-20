#!/usr/bin/node

const strToInt = parseInt(process.argv[2], 10);

if (isNaN(strToInt)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + strToInt);
}
