#!/usr/bin/node

const arg = process.argv;

function fact (nbr) {
  if ((nbr && nbr === 0) || (!nbr)) {
    return 1;
  }
  return nbr * fact(nbr - 1);
}
console.log(fact(parseInt(arg[2])));
