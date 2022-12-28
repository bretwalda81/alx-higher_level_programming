#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
    // The instructions want these two conditionals together
	if (parseInt(w) > 0 && parseInt(h) > 0) {
	    this.width = w;
	    this.height = h;
	}
    }
}

module.exports = Rectangle;
