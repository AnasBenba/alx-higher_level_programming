#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      characterUrls.forEach((characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (!charError) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
