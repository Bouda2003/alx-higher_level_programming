#!/usr/bin/node
const target = Math.floor(Number(process.argv[2]));
if (isNaN(target)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${target}`);
}
