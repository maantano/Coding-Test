// 5
// 1 1
// 2 3
// 3 4
// 9 8
// 5 2
// [5]
// [1 1]
// [2 3]
// [3 4]
// [9 8]
// [5 2]

let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0]);

for (let i = 1; i <= n; i++) {
  let [a, b] = input[i].split(" ");
  console.log(`Case #${i}: ${Number(a) + Number(b)}`);
}
