// # 덩치 7568
// let n = 5;
// let arr = [
//   [55, 185],
//   [58, 183],
//   [88, 186],
//   [60, 175],
//   [46, 155],
// ];
// let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin")
// 	.toString()
// 	.trim()
// 	.split("\n")
// 	.map((el) => el.split(" ").map((el) => Number(el)));
// let [n,...arr]=input

// answer = [];
// for (let i = 0; i < n; i++) {
//   let grade = 1;
//   for (let j = 0; j < n; j++) {
//     if (i !== j) {
//       if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) grade++;
//     }
//   }
//   answer.push(grade);
// }
// console.log(answer.join(' '));

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

// const fs = require('fs');
// const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
// let input = fs.readFileSync(filePath).toString().trim().split('\n');

// const [L, C] = input.shift().split(' ').map(Number);
// const alphabet = input.shift().split(' ').sort();
// const vowel = ['a', 'e', 'i', 'o', 'u'];

// const n = 4;
// const m = 6;
// const arr = ["a", "t", "c", "i", "s", "w"];
// arr.sort((a, b) => a - b);
// const vowel = ["a", "e", "i", "o", "u"];
// answer = [];

// function backTracking(str, startIndex) {
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
//     for (let i = startIndex; i < m; i++) {
//       backTracking(str + arr[i], i + 1);
//     }
//   }
// }
// backTracking("", 0);
// console.log(answer.join("\n"));

// #  N-QUEENS 9663

// let N = 8;

// let answer = 0;
// let row = Array.from({ length: N + 1 }, () => 0);
// console.log(row);
// function chk(L) {
//   for (let i = 0; i < L; i++) {
//     if (Math.abs(row[L] - row[i]) === L - i || row[L] === row[i]) return false;
//   }
//   return true;
// }

// function dfs(L) {
//   if (L === N) {
//     answer++;
//   } else {
//     for (let i = 0; i < N; i++) {
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

// const cal = [
//   (a, b) => a + b,
//   (a, b) => a - b,
//   (a, b) => a * b,
//   (a, b) => parseInt(a / b),
// ];

// let max = Number.MIN_SAFE_INTEGER;
// let min = Number.MAX_SAFE_INTEGER;

// function dfs(total, idx) {
//   if (idx === n - 1) {
//     min = Math.min(min, total);
//     max = Math.max(max, total);
//   } else {
//     for (let i = 0; i < unitl.length; i++) {
//       if (unitl[i] === 0) continue;
//       else {
//         unitl[i]--;
//         dfs(cal[i](total, arr[idx + 1]), idx + 1);
//         unitl[i]++;
//       }
//     }
//   }
// }
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

// dx = [-1, 1, 0, 0];
// dy = [0, 0, -1, 1];

// let min = Number.MAX_SAFE_INTEGER;
// let visited = Array.from({ length: n }, () => Array(n).fill(0));
// console.log(visited);
// function dfs(idx,total){
// 	if (idx == m){
// 		min = total
// 		return
// 	}else{
// 		for(let i =0;i<n;i++){
// 			for(let j =0; j< n; j++){

// 			}
// 		}
// 		if(arr[i][j] === 2){
// 			arr[i][j] = 0
// 			dfs(idx+1,total)
// 			arr[i][j] = 2
// 		}
// 	}

// }
// for (let i = 0; i < n; i++) {
//   for (let j = 0; j < n; j++) {
//     if (city[i][j] === 1) house.push([i, j]);
//     else if (city[i][j] === 2) chicken.push([i, j]);
//   }
// }

// const getMinDistance = () => {
//   let sum = 0;
//   house.forEach(([hx, hy]) => {
//     let min = Infinity;
//     chicken.forEach((_, index) => {
//       if (check[index] === true) {
//         const [cx, cy] = chicken[index];
//         min = Math.min(min, Math.abs(hx - cx) + Math.abs(hy - cy));
//       }
//     });
//     sum += min;
//   });
//   return sum;
// };

// const check = new Array(chicken.length).fill(false);
// let answer = Infinity;

// const DFS = (idx, cnt) => {
//   if (cnt === m) {
//     answer = Math.min(answer, getMinDistance());
//     return;
//   } else {
//     for (let i = idx; i < chicken.length; i++) {
//       if (check[i] === true) continue;
//       check[i] = true;
//       DFS(i, cnt + 1);
//       check[i] = false;
//     }
//   }
// };
// DFS(0, 0);
// console.log(answer);

// ================================================================
// let john = { name: "John" };

// let visitsCountObj = {}; // 객체 생성

// visitsCountObj[john] = 123;
// console.log(visitsCountObj[john]);
// console.log(visitsCountObj["[object Object]"]);

const C = {
  A(data) {
    console.log("---------A------------");
    console.log(data);
    console.log(this);
  },

  //   B(data) => {
  //     console.log("---------B------------");
  //     console.log(data);
  //     console.log(this);
  //   };
};

C.A("A");
// C.B("B");
