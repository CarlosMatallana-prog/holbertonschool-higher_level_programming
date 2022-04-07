#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = typeof c === 'undefined' ? 'X' : c;
    for (let i = this.height; i > 0; i--) {
      console.log(`${c}`.repeat(this.width));
    }
  }
}

module.exports = Square;
