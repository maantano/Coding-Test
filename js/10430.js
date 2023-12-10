const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(Number);
const a = input[0];
const b = input[1];
const c = input[2];

console.log((a + b) % c);
console.log(((a % c) + (b % c)) % c);
console.log((a * b) % c);
console.log(((a % c) * (b % c)) % c);

// var fs = require('fs');
// var input = fs.readFileSync('/dev/stdin').toString().split(' ');
// var a = parseInt(input[0]);
// var b = parseInt(input[1]);
// var c = parseInt(input[2]);

// console.log((a+b)%c);
// console.log( ((a%c)+(b%c))%c );
// console.log( (a*b%c) );
// console.log( ((a%c)*(b%c))%c );
