#!/usr/bin/node

const c = process.argv.length;

if (c < 3) {
  console.log('No argument');
} else if (c === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
