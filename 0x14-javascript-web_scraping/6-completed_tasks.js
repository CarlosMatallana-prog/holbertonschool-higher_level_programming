#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, values) => {
  if (error) return console.log(error);
  const results = JSON.parse(values);
  const completed = {};
  for (const result of results) {
    if (result.completed) {
      if (completed[result.userId]) {
        completed[result.userId] += 1;
      } else {
        completed[result.userId] = 1;
      }
    }
  }
  console.log(completed);
});
