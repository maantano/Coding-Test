let [count, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");
// input = [2, 6, 12];

result = [];
for (let i = 0; i < count; i++) {
  const len = Number(arr[i]) + 1;
  const dp = new Array(len).fill(0);
  dp[1] = dp[2] = dp[3] = 1;

  for (let j = 4; j < dp.length; j++) {
    dp[j] = dp[j - 3] + dp[j - 2];
  }
  result.push(dp[arr[i]]);
}

console.log(result.join("\n"));
