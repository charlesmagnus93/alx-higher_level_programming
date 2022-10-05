#!/usr/bin/node

const { readFileSync, writeFileSync } = require('fs');

const content1 = readFileSync('fileA.txt', 'utf-8');
const content2 = readFileSync('fileB.txt', 'utf-8');
writeFileSync('fileC.txt', content1 + '\n' + content2, 'utf-8');
