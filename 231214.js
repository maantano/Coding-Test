// let stdin = require('fs').readFileSync('/dev/stdin').toString().trim()
// let input = stdin.split('\n').map((item)=>item.split(' ').Number(item))
// const [n,...arr] = input;
// let [n, ...arr] = require("fs")
//   .readFileSync("input.txt")
//   .toString()
//   .split("\n")
//   .map((v) => v.split(" ").map((v) => +v)); //.map((v) => Number(v)
let n = 7;
let arr = [
  [3, 10],
  [5, 20],
  [1, 10],
  [1, 20],
  [2, 15],
  [4, 40],
  [2, 200],
];
let dp = Array(n).fill(0);
console.log(arr[2][0]);

for (let i = 0; i < n + 1; i++) {
  for (let j = i + arr[i][0]; j < n + 1; j++) {
    console.log(arr[i][0] + i);

    if (dp[j] < dp[i] + arr[i][1]) {
      dp[j] = dp[i] + arr[i][1];
    }
  }
}
console.log(dp);
