// # #9095 1,2,3 더하기

// input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .split("\n")
//   .map(Number);
// let [n, ...arr] = input;
// let dp = Array.from({ length: 12 }, () => 0);

// dp[1] = 1;
// dp[2] = 2;
// dp[3] = 4;

// for (let i = 4; i <= 12; i++) {
//   dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
// }
// arr.forEach((el) => {
//   console.log(dp[el]);
// });

// n = Number(require("fs").readFileSync("/dev/stdin").toString());

// dp = Array.from({ length: 1001 }, () => 0);

// dp[1] = 1;
// dp[2] = 2;
// for (let i = 3; i < 1001; i++) {
//   dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
// }
// console.log(dp[n]);
