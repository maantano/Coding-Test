// # 덩치 7568

// let fs = require("fs");
// let input = fs
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((el) => el.split(" ").map((el) => Number(el)));
// let [n, ...arr] = input;
// answer = [];
// for (let i = 0; i < n; i++) {
//   let grade = 1;
//   for (j = 0; j < n; j++) {
//     if (i !== j) {
//       if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) grade++;
//     }
//   }
//   answer.push(grade);
// }
// console.log(answer.join(" "));

// # 체스판 다시 칠하기 1018
// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// const NM = input.shift().split(" ");
// const N = Number(NM.shift());
// const M = Number(NM.shift());
// const candidates = [];

// const whiteFirstBoard = [
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
// ];

// const blackFirstBoard = [
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
//   "BWBWBWBW",
//   "WBWBWBWB",
// ];

// function paintWhiteFirst(x, y) {
//   let count = 0;

//   for (let i = y; i < y + 8; i++) {
//     for (let j = x; j < x + 8; j++) {
//       if (input[i][j] !== whiteFirstBoard[i - y][j - x]) {
//         count++;
//       }
//     }
//   }

//   return count;
// }

// function paintBlackFirst(x, y) {
//   let count = 0;

//   for (let i = y; i < y + 8; i++) {
//     for (let j = x; j < x + 8; j++) {
//       if (input[i][j] !== blackFirstBoard[i - y][j - x]) {
//         count++;
//       }
//     }
//   }

//   return count;
// }

// for (let i = 0; i + 7 < N; i++) {
//   for (let j = 0; j + 7 < M; j++) {
//     candidates.push(paintWhiteFirst(j, i));
//     candidates.push(paintBlackFirst(j, i));
//   }
// }

// console.log(Math.min(...candidates));

// 암호 만들기 1759

// const fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const [n, m] = input.shift().split(" ").map(Number);
// const arr = input.shift().split(" ").sort();
// const vowel = ["a", "e", "i", "o", "u"];
// answer = [];
// function bt(idx, str) {
//   if (str.length === n) {
//     let cnt = 0;
//     for (let i = 0; i < str.length; i++) {
//       if (vowel.includes(str[i])) {
//         cnt++;
//       }
//     }
//     if (cnt > 0 && n - cnt > 1) {
//       answer.push(str);
//     }
//     return;
//   } else {
//     for (let i = idx; i < m; i++) {
//       bt(i + 1, str + arr[i]);
//     }
//   }
// }
// bt(0, "");
// console.log(answer.join("\n"));

// #  N-QUEENS 9663
// let n = 8;
// let answer = 0;
// let row = Array.from({ length: n + 1 }, () => 0);

// function chk(L) {
//   for (let i = 0; i < L; i++) {
//     if (Math.abs(row[L] - row[i]) === L - i || row[L] === row[i]) return false;
//   }
//   return true;
// }

// function dfs(L) {
//   if (L === n) {
//     answer++;
//   } else {
//     for (let i = 0; i < n; i++) {
//       row[L] = i;
//       if (chk(L)) dfs(L + 1);
//     }
//   }
// }
// dfs(0);
// console.log(answer);

// # 연산자 끼워넣기 14888

// const n = 2;
// const arr = [5, 6];
// let unitl = [0, 0, 1, 0];
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map((el)=>el.split(' ').map((el)=>Number(el)))
// let [n,arr,unitl] = input

// const cal = [
//   (a, b) => a + b,
//   (a, b) => a - b,
//   (a, b) => a * b,
//   (a, b) => parseInt(a / b),
// ];
// let max = Number.MIN_SAFE_INTEGER;
// let min = Number.MAX_SAFE_INTEGER;
// const dfs = (total, idx) => {
//   if (idx === n - 1) {
//     min = Math.min(total, min);
//     max = Math.max(total, max);
//   } else {
//     for (let i = 0; i < 4; i++) {
//       if (unitl[i] === 0) continue;
//       unitl[i]--;
//       dfs(cal[i](total, arr[idx + 1]), idx + 1);
//       unitl[i]++;
//     }
//   }
// };
// dfs(arr[0], 0);
// console.log(max ? max : 0);
// console.log(min ? min : 0);

// # 치킨 배달 15686

n = 5;
m = 3;
city = [
  [0, 0, 1, 0, 0],
  [0, 0, 2, 0, 1],
  [0, 1, 2, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 2],
];

const house = [];
const chicken = [];
const check = new Array(chicken.length).fill(false);
let answer = Infinity;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (city[i][j] == 1) house.push([i, j]);
    else if (city[i][j] == 2) chicken.push([i, j]);
  }
}

const getMinDistance = () => {
  let sum = 0;
  house.forEach(([hx, hy]) => {
    let min = Infinity;
    chicken.forEach((_, idx) => {
      if (check[idx] === true) {
        const [cx, cy] = chicken[idx];
        min = Math.min(min, Math.abs(hx - cx) + Math.abs(hy - cy));
      }
    });
    sum += min;
  });
  return sum;
};

const dfs = (idx, cnt) => {
  if (cnt === m) {
    answer = Math.min(answer, getMinDistance());
    return;
  } else {
    for (let i = idx; i < chicken.length; i++) {
      if (check[i] === true) continue;
      check[i] = true;
      dfs(i, cnt + 1);
      check[i] = false;
    }
  }
};
dfs(0, 0);
console.log(answer);
