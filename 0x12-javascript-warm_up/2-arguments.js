#!/usr/bin/node
'use strict';
const num_arguments = process.argv.length;
if (num_arguments === 2) {
  console.log('No argument');
} else if (num_arguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
