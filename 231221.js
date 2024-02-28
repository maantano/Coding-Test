// 11399 # ATM
// n = 5;
// arr = [3, 1, 4, 3, 2];

// let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
// let N = Number(input[0]);
// let arr = input[1].split(" ").map(Number);
// arr.sort((a, b) => a - b);
// answer = [];
// tmp = 0;
// arr.forEach((el) => {
//   tmp += el;
//   answer.push(tmp);
// });

// console.log(answer.reduce((acc, cur) => acc + cur));

// let input = require('fs').readFileSync('/dev/stdin').toString().split('/n')
// let [chk,...arr] = input
// let n = chk[0]
// let target = chk[1]

// let n = 10;
// let target = 4200;
// let arr = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000];
// dp = Array.from({ length: n + 1 }, () => 0);
// console.log(dp);

// for(let i=1;i<=n;i++){
//   dp[i] = Math.min(target/arr[i-1],target/arr[i])
// }

// 11047  # 돈전 0
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// let [n, ...arr] = input;
// let [num, target] = n.split(' ');
// target = Number(target);

// solution(n, target, arr);

// function solution(n, target, arr) {
//   let result = 0;
//   for (let i = arr.length - 1; i >= 0; i--) {
//     if (target - arr[i] >= 0) {
//       result += Math.floor(target / arr[i]);
//       target = target % arr[i];
//     }
//   }
//   console.log(result);
// }

// 1931 #회의실 배정

// const n = 11;
// const arr = [
//   [1, 4],
//   [3, 5],
//   [0, 6],
//   [5, 7],
//   [3, 8],
//   [5, 9],
//   [6, 10],
//   [8, 11],
//   [8, 12],
//   [2, 13],
//   [12, 14],
// ];
// const arr = [
//   "1 4",
//   "3 5",
//   "0 6",
//   "5 7",
//   "3 8",
//   "5 9",
//   "6 10",
//   "8 11",
//   "8 12",
//   "2 13",
//   "12 14",
// ];

// 1931 # 회의실 배정
// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const [n, ...arr] = input;
// let answer = 0;
// const times = arr
//   .map((num) => num.split(" ").map((num) => +num))
//   .sort((a, b) => {
//     if (a[1] === b[1]) {
//       return a[0] - b[0];
//     } else {
//       return a[1] - b[1];
//     }
//   });
// let et = 0;

// times.forEach((time) => {
//   if (time[0] >= et) {
//     answer++;
//     et = time[1];
//   }
// });
// console.log(answer);

// #1026 보물

// n = 5;
// arrA = [1, 1, 1, 6, 0];
// arrB = [2, 7, 8, 3, 1];

// n = 3;
// arrA = [1, 1, 3];
// arrB = [10, 30, 20];

// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
// let n = Number(input[0])
// let arrA = input[1].split(' ').map(Number)
// let arrB = input[2].split(' ').map(Number)

// arrA.sort((a, b) => a - b);
// arrB.sort((a, b) => b - a);
// answer = 0;
// for (let i = 0; i < n; i++) {
//   answer += arrA[i] * arrB[i];
// }
// console.log(answer);

// 2217 # 로프
// let input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map(Number);
// let [n, arr] = input;
// arr.sort((a, b) => b - a);
// answer = [];
// for (let i = 0; i < n; i++) {
//   answer.push(arr[i] * (i + 1));
// }
// console.log(Math.max(...answer));

// 1789 # 수들의 합

n = 200;
let n = Number(require("fs").readFileSync("/dev/stdin").trim());
answer = 0;
idx = 1;
cnt = 0;
while (true) {
  answer += idx;
  idx++;
  cnt++;
  if (answer > n) {
    cnt--;
    break;
  }
}
console.log(cnt);
