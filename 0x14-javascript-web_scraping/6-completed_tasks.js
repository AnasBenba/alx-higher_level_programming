#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const todosData = JSON.parse(body);
      const completedTasksByUser = {};

      todosData.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId.toString();
          completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
        }
      });

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
