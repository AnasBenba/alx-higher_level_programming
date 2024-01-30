#!/usr/bin/node

const request = require('request');

const makeRequest = (apiUrl) => {
  return new Promise((resolve, reject) => {
    request(apiUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

const countMoviesWithWedge = (results) => {
  return results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0);
};

// Main function
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
