#!/usr/bin/node

const baseSquare = require('./5-square');
class Square extends baseSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
        for (let i = 0; i < this.height; i++) {
          let output = '';
          for (let y = 0; y < this.width; y++) {
            output += c;
          }
          console.log(output);
        }
    }
  }
}
module.exports = Square;
