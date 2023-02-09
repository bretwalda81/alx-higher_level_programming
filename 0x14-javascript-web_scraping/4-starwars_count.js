#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request.get(url, function (err, reply, body) {
    if (err) throw err;
    let count = 0;

    for (const movieName of JSON.parse(body).results) {
	for (const character of movieName.characters) {
	    if (character.includes('18')) {
		count++;
	    }
	}
    }
    console.log(count);
});
