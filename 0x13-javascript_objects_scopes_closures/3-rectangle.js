#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	if (parseInt(h) > 0 && parseInt(w) > 0) {
	    this.height = h;
	    this.width = w;
	}
    }
}

Rectangle.prototype.print = function () {
    let i = 0;
    for (i; i < this.height; i++) {
	console.log('X'.repeat(this.width));
    }
};

module.exports = Rectangle;
