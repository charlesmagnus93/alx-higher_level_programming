#!/usr/bin/node

const arg = process.argv;

if ((arg[2] && Number.isInteger(parseInt(arg[2])))) {
  for (let i = 0; i < parseInt(arg[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
