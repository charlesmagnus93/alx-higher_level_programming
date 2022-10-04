#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(parseInt(arg[2]), parseInt(arg[3]));
