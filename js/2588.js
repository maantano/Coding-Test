// const input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number)

// const lenA = Math.floor(input[0] / 10)

// const lenB = Math.floor(input[1] / 10);
// let answer = 0;
// for (let i = 1; i <= lenB; i++) {
//   console.log(input[0] * (input[0] % (i * 10)));
//   answer += (input[0] * input[0]) % (i * 10);
// }

// console.log(answer);

const fs = require("fs");
const [num1, num2] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map(Number);

const oneNum = num2 % 10;
const tenNum = Math.floor((num2 % 100) / 10);
const hundredNum = Math.floor(num2 / 100);

console.log(num1 * oneNum);
console.log(num1 * tenNum);
console.log(num1 * hundredNum);
console.log(num1 * num2);
