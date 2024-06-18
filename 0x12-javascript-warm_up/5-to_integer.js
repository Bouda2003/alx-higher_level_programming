#!/usr/bin/node
const target = process.argv[2];
if (isNaN(target)) {
  console.log('Not a number');
} else {
  console.log(Math.floor(Number(target)));
}
