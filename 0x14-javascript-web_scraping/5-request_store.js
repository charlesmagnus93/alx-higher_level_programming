#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv.slice(2)[0];
const filePath = process.argv.slice(2)[1];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, () => {});
});
