#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	if (parseInt(h) > 0) {
	    this.height = h;
	}
	if (parseInt(w) > 0) {
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

Rectangle.prototype.double = function () {
    this.height *= 2;
    this.width *= 2;
};

Rectangle.prototype.rotate = function () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
};

module.exports = Rectangle;
