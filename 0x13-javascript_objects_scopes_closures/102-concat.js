#!/usr/bin/node
const files = require('files');
const a = files.readFileSync(process.argv[2], 'utf8');
const b = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], a + b);
