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

// N = 6;
// board = [
//   [0, 1, 2, 3, 4, 5],
//   [1, 0, 2, 3, 4, 5],
//   [1, 2, 0, 3, 4, 5],
//   [1, 2, 3, 0, 4, 5],
//   [1, 2, 3, 4, 0, 5],
//   [1, 2, 3, 4, 5, 0],
// ];

// input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .split("\n")
//   .map((el) => el.split(" ").map(Number));
// let [N, ...board] = input;

// visited = Array.from({ length: N + 1 }, () => 0);
// answer = [];

// function DFS(L, idx) {
//   if (L === N / 2) {
//     A = 0;
//     B = 0;
//     for (let i = 0; i < N; i++) {
//       for (let j = 0; j < N; j++) {
//         if (visited[i] && visited[j]) {
//           A += board[i][j];
//         } else if (!visited[i][j] && !visited[j]) {
//           B += board[i][j];
//         }
//       }
//     }
//     answer.push(Math.abs(A - B));
//     return;
//   }
//   for (let i = idx; i < N; i++) {
//     visited[i] = true;
//     DFS(L + 1, i + 1);
//     visited[i] = false;
//   }
// }

// DFS(0, 0);
// console.log(Math.min(...answer));

const sol = (input) => {
  const N = +input[0];
  const halfN = N / 2;
  const stats = input.slice(1).map((str) => str.split(" ").map(Number));

  const check = new Array(N).fill(0);
  let min = Number.MAX_SAFE_INTEGER;
  function dfs(L, K) {
    if (L === halfN) {
      // 스타트팀에 N/2 명이 뽑혔다면
      const sTeam = [];
      const lTeam = [];
      let sSum = (lSum = 0);
      for (let i = 0; i < N; i++) {
        if (check[i]) sTeam.push(i);
        // 체크 배열은 스타트 팀에 넣어주고, 체크 배열에 없으면 링크 팀에 넣어준다.
        else lTeam.push(i);
      }
      for (let i = 0; i < halfN; i++) {
        for (let j = i + 1; j < halfN; j++) {
          // (i,j), (j,i) 쌍을 계속 더해준다.
          sSum = sSum + stats[sTeam[i]][sTeam[j]] + stats[sTeam[j]][sTeam[i]];
          lSum = lSum + stats[lTeam[i]][lTeam[j]] + stats[lTeam[j]][lTeam[i]];
        }
      }
      min = Math.min(min, Math.abs(sSum - lSum));
      return;
    }

    for (let i = K; i < N; i++) {
      // 체크 배열을 스타트 팀 구성에 사용한다.
      check[i] = 1;
      dfs(L + 1, i + 1);
      check[i] = 0;
    }
  }
  dfs(0, 0);
  return min;
};

// 백준에서 입력을 받는 코드
const input = [];
require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    console.log(sol(input));
    process.exit();
  });
