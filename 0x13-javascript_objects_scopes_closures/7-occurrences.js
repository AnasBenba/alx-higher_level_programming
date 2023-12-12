#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let i = 0;
  let result = 0;
  while (i < len) {
    if (searchElement === list[i]) {
      result++;
    }
    i++;
  }
  return result;
};
