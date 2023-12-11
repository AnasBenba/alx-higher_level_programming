#!/usr/bin/node

let i = 0;
process.argv.forEach(function (pro) {
  i++;
});

if (i <= 2) {
  console.log('No argument');
} else if (i === 3) {
  console.log(process.argv[2]);
}
