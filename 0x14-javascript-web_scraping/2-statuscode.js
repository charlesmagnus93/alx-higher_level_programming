#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
