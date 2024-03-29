#!/usr/bin/node

const Square0 = require('./5-square');

module.exports = class Square extends Square0 {
  charPrint (c) {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        if (c) {
          str += c;
        } else {
          str += 'X';
        }
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
