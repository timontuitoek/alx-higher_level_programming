#!/usr/bin/node

//checks number of arguments
const numArguments = process.argv.length - 2//subtracting by 2 to exclude node and script file name

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
