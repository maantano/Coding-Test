// 5
// 1 1
// 2 3
// 3 4
// 9 8
// 5 2

let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let [n, ...arr] = input;

for (let i = 0; i < n; i++) {
  let [a, b] = input[0].split(" ");
  console.log("123");
  console.log(a, b);
}
