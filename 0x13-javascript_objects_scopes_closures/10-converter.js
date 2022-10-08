#!/usr/bin/node

exports.converter = function (base) {
  return (value) => {
    if (base === 10) {
      return parseInt(value, base);
    } else {
      return value.toString(base);
    }
  };
};
