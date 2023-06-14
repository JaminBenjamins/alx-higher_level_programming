#!/usr/bin/node
const { argv } = require('process');
const size = Number(argv[2]);
const repeat = 'x'.repeat(size);
if (isNan(size)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < size; i++) {
		console.log(repeat);
	}
}
