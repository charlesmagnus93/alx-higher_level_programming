#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let i = 1; i < list.length; i++) {
    newList.push(list[list.length - i]);
  }
  newList.push(list[0]);
  return newList;
};
