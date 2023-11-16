#!/usr/bin/node

const { dict } = require('./101-data');

const computeDict = (inputDict) => {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurences = inputDict[userId];

    if (!resultDict[occurences]) {
      resultDict[occurences] = [];
    }

    resultDict[occurences].push(userId);
  }

  return resultDict;
};

const newDict = computeDict(dict);

console.log(newDict);
