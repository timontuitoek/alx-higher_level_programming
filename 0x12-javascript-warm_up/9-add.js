#!/usr/bin/node

function add (c, d) {
  return parseInt(c, 10) + parseInt(d, 10);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(add(arg1, arg2));
