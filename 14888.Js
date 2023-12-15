// let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

// let n = Number(input[0])
// let arr = input[1].split(' ').map(Number)
// let unitl = input[2].split(' ').map(Number)
let n = 2;
let arr = [5, 6];
let unitl = [0, 0, 1, 0];

const calculator = [
  (a, b) => a + b,
  (a, b) => a - b,
  (a, b) => a * b,
  (a, b) => parseInt(a / b),
];

let max = Number.MIN_SAFE_INTEGER;
let min = Number.MAX_SAFE_INTEGER;

const dfs = (total, idx) => {
  if (idx === n - 1) {
    min = Math.min(min, total);
    max = Math.max(max, total);
  } else {
    for (let i = 0; i < unitl.length; i++) {
      if (unitl[i] === 0) {
        continue;
      } else {
        unitl[i]--;
        dfs(calculator[i](total, arr[idx + 1]), idx + 1);
        unitl[i]++;
      }
    }
  }
};
dfs(arr[0], 0);
console.log(max ? max : 0);
console.log(min ? min : 0);

// let N = 2;
// let nums = [5, 6];
// let operator = [0, 0, 1, 0];

// let max = Number.MIN_SAFE_INTEGER;
// let min = Number.MAX_SAFE_INTEGER;

// const calculator = [
//   (a, b) => a + b,
//   (a, b) => a - b,
//   (a, b) => a * b,
//   (a, b) => parseInt(a / b),
// ];

// const dfs = (count, result) => {
//   //연산자 갯수만큼 반복하다가 max, min 판정
//   if (count === N - 1) {
//     max = Math.max(max, result);
//     min = Math.min(min, result);
//   } else {
//     for (let i = 0; i < operator.length; i++) {
//       if (operator[i] === 0) {
//         continue;
//       }
//       operator[i]--;
//       dfs(count + 1, calculator[i](result, nums[count + 1]));
//       //배열 원상복구
//       operator[i]++;
//     }
//   }
// };

// dfs(0, nums[0]);

// console.log(max ? max : 0);
// console.log(min ? min : 0);
