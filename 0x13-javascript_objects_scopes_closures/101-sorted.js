#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const arr = [];
let i = 0;
let y = 0;
for (const key in dict) {
  arr[i] = dict[key];
  i++;
}
i = 0;
const uniqueArr = [...new Set(arr)];
while (i < uniqueArr.length) {
  const k = uniqueArr[i].toString();
  newDict[k] = [];
  for (const key in dict) {
    if (uniqueArr[i] === dict[key]) {
      newDict[k][y] = key;
      y++;
    }
  }
  i++;
  y = 0;
}
console.log(newDict);
