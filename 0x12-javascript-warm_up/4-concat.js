#!/usr/bin/node
const { argv } = require('process');
const argv1 = argv[2]; const argv[2] = argv[3];
console.log(argv1 + ' is ' + argv2);
