#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log('0');
} else {
  process.argv.sort(function (a, b) {
    return a - b;
  });
  console.log(process.argv[len - 2]);
}
