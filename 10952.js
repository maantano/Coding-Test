let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let idx = 0;
while (1) {
  let [a, b] = input[idx].split(" ");
  if (a === 0 && b === 0) {
    break;
  }
  console.log(Number(a) + Number(b));
  idx++;
}
