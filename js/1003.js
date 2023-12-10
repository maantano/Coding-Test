const fs = require("fs");

// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const input = [3, 0, 1, 3];
// const len = input.shift();
const [n, ...arr] = input;
// console.log(input);
// console.log(len);

for (let i = 0; i < n; i++) {
  let oneCount = 0,
    zeroCount = 1;
  for (let j = 1; j <= arr[i]; j++) {
    const tmpCnt = zeroCount;
    zeroCount = oneCount;
    oneCount = tmpCnt + oneCount;
  }
  console.log(zeroCount + " " + oneCount);
}
