#!/usr/bin/node
exports.addMeMaybe = function (number, callMe) {
  callMe(++number);
};
