#!/usr/bin/node

const list = require('./100-data').list;
const arr = [];
const len = list.length;
list.map(function (element, index) {
  if (index < len) {
    arr[index] = element * index;
  }
  return arr;
});

console.log(list);
console.log(arr);
