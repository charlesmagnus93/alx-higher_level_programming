#!/usr/bin/node

const request = require('request');
const movieID = process.argv.slice(2)[0];

request(`https://swapi-api.hbtn.io/api/films/${movieID}`, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
