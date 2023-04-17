#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(file1, function (err, data) {
  if (err) throw err;
  fs.appendFile(dest, data, function (err) {
    if (err) throw err;
    fs.readFile(file2, function (err, data) {
      if (err) throw err;
      fs.appendFile(dest, data, function (err) {
        if (err) throw err;
        console.log('The two files were concatenated successfully!');
      });
    });
  });
});
