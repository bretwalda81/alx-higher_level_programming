#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, reply, body) {
  if (err) throw err;

  const userList = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (userList[task.userId]) {
        userList[task.userId]++;
      } else {
        userList[task.userId] = 1;
      }
    }
  }
  console.log(userList);
});
