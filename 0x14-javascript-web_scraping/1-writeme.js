#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv.slice(2)[0]
const text = process.argv.slice(2)[1];

fs.writeFile(filePath, text, {flag: 'w+'}, () => {});
