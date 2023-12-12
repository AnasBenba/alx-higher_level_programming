#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  let i = 0;
  let y = 0;
  let temp = 0;
  while (i < len) {
    temp = list[i];
    while (y < len) {
      if (y === len - 1) {
        list[i] = list[y];
        list[y] = temp;
      }
      y++;
    }
    len--;
    i++;
    y = 0;
  }
  return list;
};
