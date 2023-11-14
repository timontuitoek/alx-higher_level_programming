#!/usr/bin/node
'use strict';
const Num_Arguments = process.argv.length;
if (Num_Arguments === 2) {
  console.log('No argument');
} else if (Num_Arguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
