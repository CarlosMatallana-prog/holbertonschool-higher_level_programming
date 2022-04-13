#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, values) => {
  if (error) return (console.log(error));
  const movies = JSON.parse(values).results;
  let count = 0;

  for (let i = 0; i < movies.length; i++) {
    for (let j = 0; j < movies[i].characters.length; j++) {
      if (movies[i].characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
