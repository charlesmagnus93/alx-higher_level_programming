#!/usr/bin/node

const Square0 = require('./5-square');

module.exports = class Square extends Square0 {
  charPrint (c) {
    if (c) {}
    let str = '';
    const caracter = c ? 'C' : 'X';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        str += caracter;
      }
      if (i === (this.height - 1)) {
        str += '';
      } else {
        str += '\n';
      }
    }
    console.log(str);
  }
};
