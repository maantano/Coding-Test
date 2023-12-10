const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");
// const input = [7, 3];
const num1 = parseInt(input[0]);
const num2 = parseInt(input[1]);

console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(Math.floor(num1 / num2));
console.log(num1 % num2);

const fs = require("fs");
const data = fs.readFileSync("dev/stdin").toString().split("");

consle.log(data[0] + "??!");

// let input = require('fs').readFileSync('dev/stdin').toString().split(' ');

// const num1 = Number(num1);
// const num2 = Number(num2);

// console.log(num1 + num2);
// console.log(num1 - num2);
// console.log(num1 * num2);
// console.log(Math.floor(num1 / num2));
// console.log(num1 % num2);
