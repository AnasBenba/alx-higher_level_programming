#!/usr/bin/node

const request = require('request');

const makeRequest = apiUrl => new Promise((resolve, reject) => {
  request(apiUrl, (error, response, body) => {
    if (error) {
      reject(error);
    } else {
      resolve(body);
    }
  });
});

const countMoviesWithWedge = results => results.reduce((count, movie) => (
  movie.characters.find(character => character.endsWith('/18/'))
    ? count + 1
    : count
), 0);

const main = async () => {
  try {
    const apiUrl = process.argv[2];
    const body = await makeRequest(apiUrl);
    const results = JSON.parse(body).results;

    const moviesWithWedge = countMoviesWithWedge(results);

    console.log(moviesWithWedge);
  } catch (error) {
    console.error(error);
  }
};

main();
