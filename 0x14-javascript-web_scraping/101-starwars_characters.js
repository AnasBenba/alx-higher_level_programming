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

      Promise.all(characterUrls.map(url => {
        return new Promise((resolve, reject) => {
          request.get(url, (charError, charResponse, charBody) => {
            if (!charError) {
              const characterData = JSON.parse(charBody);
              resolve(characterData.name);
            } else {
              reject(charError);
            }
          });
        });
      })).then(characterNames => {
        characterNames.forEach(name => console.log(name));
      }).catch(err => {
        console.error(`Error: ${err}`);
      });
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
