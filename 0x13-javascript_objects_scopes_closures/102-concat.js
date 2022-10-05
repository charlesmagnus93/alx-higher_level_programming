#!/usr/bin/node

const { readFileSync, writeFileSync } = require('fs');

const content1 = readFileSync('fileA', 'utf-8');
const content2 = readFileSync('fileB', 'utf-8');
writeFileSync('fileC', content1 + '\n' + content2, 'utf-8');
