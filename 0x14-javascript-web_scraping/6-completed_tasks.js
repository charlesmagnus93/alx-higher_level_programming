#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0];

request(url, (err, response, body) => {
  if (response.statusCode !== 200) {
    return;
  }
  if (err) {
    console.log(err);
  }

  const todos = JSON.parse(body);

  const users = {};
  for (const todo of todos) {
    if (users[todo.userId] === undefined) {
      users[todo.userId] = 0;
    }

    if (todo.completed) {
      users[todo.userId] += 1;
    }
  }
  console.log(users);
});
