#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, values) => {
  if (error) console.log(error);
  console.log(JSON.parse(values).title);
});
