#!/usr/bin/node

const length = process.argv.length;
const array = [];
let value;
let i;

if (length === 2 || length === 3) {
    console.log(0);
} else {
    for (i = 2; i < length; i++) {
	value = parseInt(process.argv[i]);

    /*
      There were some issues using the sort function with NaN
      in the array. As a workaround, only push to array if
      value contains a valid integer
    */
	if (!isNaN(value)) { array.push(value); }
    }

  /*
    Since we want the 2nd largest value in the list of arguments,
    we can easily get that by sorting the array from low to high, then
    pop off the very last node. Note that sort by default sorts alphabetically,
    which causes problems, so a dummy function is passed into sort
  */
    array.sort(function (a, b) { return a - b; });
    array.pop();
    console.log(Math.max.apply(null, array));
}
