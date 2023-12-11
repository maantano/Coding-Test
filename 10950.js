let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let n = parseInt(input[0]);

for (let i = 1; i <= n; i++) {
  let data = input[i].split(" ");
  console.log(Number(data[0]) + Number(data[1]));
}
