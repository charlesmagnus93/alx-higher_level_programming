#!/usr/bin/node

const arg = process.argv;
if (arg[2] > 0) {
  if ((arg[2] && Number.isInteger(parseInt(arg[2])))) {
    let str = '';
    for (let i = 0; i < parseInt(arg[2]); i++) {
      for (let y = 0; y < parseInt(arg[2]); y++) {
        str += 'X';
      }
      if (i === (parseInt(arg[2]) - 1)) {
        str += '';
      } else {
        str += '\n';
      }
    }
    console.log(str);
  } else {
    console.log('Missing size');
  }
}
