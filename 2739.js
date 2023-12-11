input = require("fs").readFileSync("/dev/stdin").toString().map(Number);

for (let i = 1; i < 10; i++) {
  console.log(`${input} * ${i} = ${input * i}`);
}
