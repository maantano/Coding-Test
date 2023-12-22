// 1476 날짜 계산
// let input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split(" ")
//   .map(Number);
// let [e, s, m] = input;

// let chkE = 1;
// let chkS = 1;
// let chkM = 1;
// let answer = 1;

// while (true) {
//   if (chkE === e && chkS === s && chkM === m) {
//     console.log(answer);
//     break;
//   }
//   chkE = (answer % 15) + 1;
//   chkS = (answer % 28) + 1;
//   chkM = (answer % 19) + 1;
//   answer++;
// }

// #1436 영화감독 숌

// n = 2;
// let nth = 666;
// let count = 0;

// while (1) {
//   if (String(nth).includes("666")) {
//     count += 1;
//     console.log(count);
//   }
//   if (count === n) {
//     console.log(nth);
//     break;
//   }
//   nth++;
// }

// 14501 #퇴사

// n = 10;
// arr = [
//   [1, 1],
//   [1, 2],
//   [1, 3],
//   [1, 4],
//   [1, 5],
//   [1, 6],
//   [1, 7],
//   [1, 8],
//   [1, 9],
//   [1, 10],
// ];

// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map((el)=>el.split(' ').map(Number))
// let [n,...arr] = input

// dp = Array.from({ length: n + 1 }, () => 0);
// for (let i = n - 1; i > -1; i--) {
//   if (i + arr[i][0] > n) {
//     dp[i] = dp[i + 1];
//   } else {
//     dp[i] = Math.max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]]);
//   }
// }
// console.log(dp[0]);

// # 14889 스타트와 링크

N = 6;
board = [
  [0, 1, 2, 3, 4, 5],
  [1, 0, 2, 3, 4, 5],
  [1, 2, 0, 3, 4, 5],
  [1, 2, 3, 0, 4, 5],
  [1, 2, 3, 4, 0, 5],
  [1, 2, 3, 4, 5, 0],
];

visited = Array.from({ length: N + 1 }, () => 0);
answer = [];

function DFS(L, idx) {
  if (L === N / 2) {
    A = 0;
    B = 0;
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (visited[i] && visited[j]) {
          A += board[i][j];
        } else if (!visited[i][j] && !visited[j]) {
          B += board[i][j];
        }
      }
    }
    answer.push(Math.abs(A - B));
    return;
  }
  for (let i = idx; i < N; i++) {
    visited[i] = true;
    DFS(L + 1, i + 1);
    visited[i] = false;
  }
}

DFS(0, 0);
console.log(Math.min(...answer));
