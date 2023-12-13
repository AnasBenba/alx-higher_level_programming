#!/usr/bin/node

exports.converter = function (base) {
  return function conv (num) {
          let result = '';
	  let reminder = '';
	  if (num === 0) {
      return '0';
	  } else if (base !== 16) {
	    while (num > 0) {
	      reminder = num % base;
	      result = reminder.toString() + result;
	      num = Math.floor(num / base);
	    }
	  } else {
	    while (num > 0) {
              reminder = num % base;
	      if (reminder < 10) {
                result = reminder.toString() + result;
	      } else {
                result = String.fromCharCode('A'.charCodeAt(0) + reminder - 10) + result;
	      }
            num = num / base;
            num = parseInt(num);
            }
	  }
	  return result;
  };
};
