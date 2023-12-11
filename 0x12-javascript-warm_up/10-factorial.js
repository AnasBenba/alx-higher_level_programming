#!/usr/bin/node

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (process.argv.length <= 2) {
  console.log('1');
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
