#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rows = this.height;
    while (rows > 0) {
      console.log('x'.repeat(this.width));
      rows--;
    }
  }
}

module.exports = Rectangle;
