#!/usr/bin/node

const fs = require('fs');

if (process.argv.length >= 4) {
  const fileA = process.argv[2];
  const fileB = process.argv[3];
  const fileC = process.argv[4];
  const fileAcontent = fs.readFileSync(fileA, 'utf8');
  const fileBcontent = fs.readFileSync(fileB, 'utf8');
  const concFile = fileAcontent + fileBcontent;
  fs.writeFileSync(fileC, concFile, 'utf8');
}
