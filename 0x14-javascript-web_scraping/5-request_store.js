#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, values) => {
  if (error) console.log(error);
  fs.writeFile(process.argv[3], values, 'utf8', (err) => {
    if (err) console.log(err);
  });
});
