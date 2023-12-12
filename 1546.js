// // let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
// // let n = input[0]
// // let l = input[1].split('')

// n = 3;
// l = "40 80 60".split(" ").map(Number);

// l.sort((a, b) => b - a);
// // let total = l.reduce((acc, cur) => acc + cur, 0);
// let maxNum = l[0];
// let rest = l.slice(1, l.length);
// console.log(rest);
// rest = rest.map((item) => (item / maxNum) * 100);

// let total = rest.reduce((acc, cur) => acc + cur);
// console.log(total + maxNum);
// console.log((total + maxNum) / (rest.length + 1));

let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const num = input[0] * 1;
const score = input[1].split(" ");

const max = Math.max(...score);
let sum = 0;

for (let i = 0; i < num; i++) {
  sum += (score[i] / max) * 100;
}

console.log(sum / num);
