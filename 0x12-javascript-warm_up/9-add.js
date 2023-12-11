#!/usr/bin/node

function add (a, b) {
  return a + b;
}
let result = 0;

if (process.argv.length <= 3) {
  console.log('NaN');
} else {
  result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
  console.log(result);
}
