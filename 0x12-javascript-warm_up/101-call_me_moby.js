#!/usr/bin/node

exports.repeatFunction = function (x, callMe) {
  for (let i = 0; i < x; i++) {
    callMe();
  }
};
