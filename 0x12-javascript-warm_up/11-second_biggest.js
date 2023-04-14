#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const nums = args.map(Number);
  const max = Math.max(...nums);
  const secondMax = nums.filter(num => num !== max).reduce((a, b) => Math.max(a, b), -Infinity);
  console.log(secondMax);
}
