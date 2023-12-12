let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0]);

for (let i = 1; i <= n; i++) {
  a = Number(input[i].split(" ")[0]);
  b = Number(input[i].split(" ")[1]);
  console.log(`Case #${i}: ${a} + ${b} = ${a + b}`);
}
