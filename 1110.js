let input = Number(require("fs").readFileSync("/dev/stdin").toString());

let num = input;
let sum = 0;
let cnt = 0;

while (true) {
  cnt++;

  sum = Math.floor(num / 10) + (num % 10);
  num = (num % 10) * 10 + (sum % 10);
  if (num === input) {
    console.log(cnt);
    break;
  }
}
