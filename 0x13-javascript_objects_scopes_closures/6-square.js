#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  // Does nothing
}

Square.prototype.charPrint = function (c) {
    if (c === null) {
	c = 'X';
    }

    let i = 0;
    for (i; i < this.width; i++) {
	console.log(c.repeat(this.width));
    }
};

module.exports = Square;
