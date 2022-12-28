#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	if (parseInt(w) > 0 && parseInt(h) > 0) {
	    this.width = w;
	    this.height = h;
	}
    }
}

Rectangle.prototype.print = function () {
    let i = 0;
    for (i; i < this.width; i++) {
	console.log('X'.repeat(this.height));
    }
};

module.exports = Rectangle;
