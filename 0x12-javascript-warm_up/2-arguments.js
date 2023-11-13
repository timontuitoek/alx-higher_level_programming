#!/usr/bin/node

//checks number of arguments
const numArguments = process.argv.length - 2//subtract ile name node

if (numArguments === 0)
{
	console.log("No argument");
}
else if (numArguments === 1)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments found");
}
