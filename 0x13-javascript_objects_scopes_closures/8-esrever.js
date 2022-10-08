#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  if (list.length !== 0) {
    for (let i = 1; i < list.length; i++) {
      newList.push(list[list.length - i]);
    }
    newList.push(list[0]);
  }
  return newList;
};
