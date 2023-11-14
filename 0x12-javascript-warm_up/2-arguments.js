#!/usr/bin/node
'use strict';
const numarguments = process.argv.length;
if (numarguments === 2) {
  console.log('No argument');
} else if (numarguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
