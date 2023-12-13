#!/usr/bin/node

module.exports.addMeMaybe = function (number, theFunction) {
  const nb = number + 1;
  theFunction(nb);
};
