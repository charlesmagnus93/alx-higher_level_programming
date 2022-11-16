#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv.slice(2)[0];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
