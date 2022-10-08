#!/usr/bin/node

exports.nbOccurences = function (list, serchElement) {
  let occ = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === serchElement) {
      occ += 1;
    }
  }
  return occ;
};
