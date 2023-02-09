#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, reply) {
    if (err) throw err;
    console.log('code: ' + reply.statusCode);
});
