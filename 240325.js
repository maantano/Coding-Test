// function solution(arr) {
//   let answers = [...new Set(arr)];
//   console.log(answers);
//   let limit = arr.length / 2;
//   console.log(limit);
//   return answers.length > limit ? limit : answers.length;
// }

// solution([3, 3, 3, 2, 2, 4]);

// function solution(a, b) {
//   a.sort();
//   b.sort();

//   for (let i = 0; i < a.length; i++) {
//     if (a[i] != b[i]) {
//       console.log(a[i]);
//       return a[i];
//     }
//   }
// }
// // function solution(participant, completion) {
// //   participant.sort();
// //   completion.sort();

// //   for (var i = 0; i < participant.length; i++) {
// //     if (participant[i] != completion[i]) {
// //       return participant[i];
// //     }
// //   }
// // }
// let a = ["leo", "kiki", "eden"];
// let b = ["eden", "kiki"];
// console.log(solution(a, b));
// // ["leo", "kiki", "eden"], ["eden", "kiki"]

// function solution(phone_book) {
//   phone_book.sort();

//   for (let i = 0; i < phone_book.length - 1; i++) {
//     if (
//       phone_book[i] === phone_book[i + 1].substring(0, phone_book[i].length)
//     ) {
//       return false;
//     }
//   }
//   return true;
// }

// solution(["119", "97674223", "1195524421"]);
// solution(["123", "456", "789"]);
// solution(["12", "123", "1235", "567", "88"]);

// function solution(N, number) {
//   var answer = 0;
//   var use = Array.from(new Array(9), () => new Set());
//   //   console.log(use);
//   if (N == number) return 1;
//   else {
//     use.forEach((el, idx) => {
//       if (idx !== 0) el.add(Number(String(N).repeat(idx)));
//     });
//     for (var i = 1; i <= 8; i++) {
//       for (var j = 1; j < i; ++j) {
//         for (var first of use[j]) {
//           for (var second of use[i - j]) {
//             use[i].add(first + second);
//             use[i].add(first - second);
//             use[i].add(first * second);
//             use[i].add(first / second);
//           }
//         }
//       }
//       if (use[i].has(number)) return i;
//     }
//     return -1;
//   }
// }
// function solution(N, number) {
//   const dp = Array.from({ length: 9 }, () => new Set());
//   dp[1].add(N);
//   console.log(dp);

//   for (let i = 1; i <= 8; i++) {
//     dp[i].add(Number(String(N).repeat(i)));
//     for (let j = 1; j < i; j++) {
//       for (const num1 of dp[j]) {
//         for (const num2 of dp[i - j]) {
//           dp[i].add(num1 + num2);
//           dp[i].add(num1 * num2);
//           dp[i].add(num1 - num2);
//           dp[i].add(Math.floor(num1 / num2));
//         }
//       }
//     }

//     if (dp[i].has(number)) {
//       return i;
//     }
//   }

//   return -1;
// }
// console.log(solution(5, 12));

// function solution(triangle) {
//   let dp = triangle.slice();
//   //   console.log(dp);
//   for (let i = dp.length - 2; i >= -0; i--) {
//     for (let j = 0; j < dp[i].length; j++) {
//       dp[i][j] += Math.max(dp[i + 1][j], dp[i + 1][j + 1]);
//     }
//   }
//   return dp[0][0];
// }

// console.log(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));

function solution(m, n, puddles) {
  const dp = Array.from({ length: n }, () => Array(m).fill(0));
  //   const dp = Array.from({ length: n }, () => Array(m).fill(0));
  //   console.log(dp);
  dp[0][0] = 1;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 && j == 0) continue;
      if (puddles.some(([x, y]) => x == j + 1 && y === i + 1)) {
        dp[i][j] = 0;
      } else {
        dp[i][j] =
          ((i > 0 ? dp[i - 1][j] : 0) + (j > 0 ? dp[i][j - 1] : 0)) %
          1000000007;
      }
    }
  }
  return dp[n - 1][m - 1];
}

// function solution(m, n, puddles) {
//   const MOD = 1_000_000_007;
//   // n행 m열 배열 생성
//   const dp = Array.from({ length: n }, () => Array(m).fill(0));

//   dp[0][0] = 1;
//   for (let i = 0; i < n; i++) {
//     for (let j = 0; j < m; j++) {
//       if (i === 0 && j === 0) continue;
//       // 인덱스 값을 기준으로 보기에 사실상 x === j, y === i의 좌표와 같은 맥락
//       // 물 웅덩이에 빠진 경우 해당 경로 값 0으로 초기화
//       if (puddles.some(([x, y]) => x === j + 1 && y === i + 1)) {
//         dp[i][j] = 0;
//       } else {
//         // x, y이동에 필요한 걸음 % MOD(문제에서 제시)
//         dp[i][j] =
//           ((i > 0 ? dp[i - 1][j] : 0) + (j > 0 ? dp[i][j - 1] : 0)) % MOD;
//       }
//     }
//   }

//   // 우측 하단까지 필요한 경로 수 반환
//   return dp[n - 1][m - 1];
// }
console.log(solution(4, 3, [[2, 2]]));
