#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
