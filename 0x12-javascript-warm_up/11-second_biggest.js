#!/usr/bin/node

const arg = process.argv;

const list = arg.slice(2);
if (arg.length <= 3) {
  console.log(0);
} else {
  console.log(list.sort(compare).slice(-2, -1)[0]);
}

function compare (a, b) {
  return a - b;
}
