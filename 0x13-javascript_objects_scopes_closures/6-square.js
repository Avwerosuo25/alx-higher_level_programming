#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Square extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
