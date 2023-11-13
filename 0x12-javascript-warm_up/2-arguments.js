#!/usr/bin/node
'use strict';
//checks number of arguments
const num_Arguments = process.argv.length;

if (num_Arguments === 2) {
	console.log("No argument");
}
else if (num_Arguments === 3) {
	console.log("Argument found");
}
else {
	console.log("Arguments found");
}
