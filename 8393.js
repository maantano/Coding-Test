input = parseInt(require("fs").readFileSync("/dev/stdin"));

answer = 0;
for (let i = 1; i <= input; i++) {
  answer += i;
}

console.log(answer);