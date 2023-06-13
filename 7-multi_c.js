#!/usr/bin/node
const { argv } = require('process');
const occurence = Number(argv[2]);
const display = () => {
	for (let i = 0; i < occurence; i++) {
		console.log('c is fun');
	}
};
isNan(occurence)
	?(console.log('Missing number of occurrences'))
	: (display());
