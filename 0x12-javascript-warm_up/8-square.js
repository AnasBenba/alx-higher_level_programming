#!/usr/bin/node

let x = 0;
let y = 0;
let output = '';

if (process.argv.length <= 2 || Number.isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  while (x < process.argv[2]) {
    while (y < process.argv[2]) {
      output += 'X';
      y++;
    }
    y = 0;
    console.log(output);
    output = '';
    x++;
  }
}
