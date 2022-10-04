#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        str += 'X';
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
