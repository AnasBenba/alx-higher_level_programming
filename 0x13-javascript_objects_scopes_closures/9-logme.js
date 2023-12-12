#!/usr/bin/node

let result = 0;

exports.logMe = function (item) {
  console.log(`${result}: ${item}`);
  result++;
};
