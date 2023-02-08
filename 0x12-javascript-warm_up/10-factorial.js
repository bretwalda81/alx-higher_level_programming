#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
    console.log(1);
} else {
    console.log(factorial(value));
}

function factorial (value) {
    if (value < 0) {
	return -1;
    } else if (value === 0) {
	return 1;
    } else {
	return (value * factorial(value - 1));
    }
}
