#!/usr/bin/node

const [,, aArg, bArg] = process.argv;
const a = parseInt(aArg);
const b = parseInt(bArg);

function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(a, b);
