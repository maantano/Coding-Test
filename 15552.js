// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
// let n = Number(input[0])

// for (let i = 1; i <= n; i++) {
//   console.log(input[i].split(" ").reduce((acc, cur) => acc + Number(cur), 0)+'\n');
// }

let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let max = Number(input[0]);
let answer = "";

for (let i = 1; i <= max; i++) {
  let num = input[i].split(" ");
  answer += Number(num[0]) + Number(num[1]) + "\n";
}

console.log(answer);
