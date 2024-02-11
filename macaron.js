// let s = "hellllllllo";
// let ans = [];

// let chk = "";
// for (let i = 0; i < s.length; i++) {
//   let c = s[i];
//   if (ans.length > 0 && ans[ans.length - 1] === c) {
//     chk = c;
//     ans.push("*");
//   } else {
//     if (chk === c) {
//       continue;
//     }
//     ans.push(c);
//     chk = c;
//   }
// }
// console.log(ans.join(""));

// 2번
// function solution(v)
// {
//     let n = v.length;
//     let m = v[0].length;
//     let dx = [-1, 1, 0, 0];
//     let dy = [0, 0, -1, 1];

//     let visited = Array.from({length: n}, () => Array(m).fill(0));
//     let ans = 0;
//     function bfs(x, y, visited) {
//         let q = [[x, y]];
//         visited[x][y] = 1;
//         let cnt = 1;
//         while (q.length > 0) {
//             [x, y] = q.shift();

//             for (let i = 0; i < 4; i++) {
//                 let nx = dx[i] + x;
//                 let ny = dy[i] + y;

//                 if (0 <= nx && nx < n && 0 <= ny && ny < m) {
//                     if (!visited[nx][ny] && v[nx][ny]) {
//                         visited[nx][ny] = 1;
//                         cnt++;
//                         q.push([nx, ny]);
//                     }
//                 }
//             }
//         }
//         return cnt;
//     }

//     let answer = [];
//     for (let i = 0; i < n; i++) {
//         for (let j = 0; j < m; j++) {
//             if (v[i][j] && !visited[i][j]) {
//                 answer.push(bfs(i, j, visited));
//             }
//         }
//     }
//     if (!answer.length) return [0, 0];
//     return [answer.length, Math.max(...answer)];
// }

// 3번.
// function calDist(seat, visited) {
//     const [row, col] = seat;
//     let minDist = Infinity;
//     for (const s of visited) {
//         const [allocatedRow, allocatedCol] = s;
//         const dist = Math.abs(row - allocatedRow) + Math.abs(col - allocatedCol);
//         minDist = Math.min(minDist, dist);
//     }
//     return minDist;
// }

// const answer = [];

// function chkSeats(n) {
//     const answer = [];
//     const visited = [[1, 1]];

//     for (let i = 1; i < n * n; i++) {
//         let dist = -1;
//         let next = [0, 0];

//         for (let i = 1; i <= n; i++) {
//             for (let j = 1; j <= n; j++) {
//                 const seat = [i, j];
//                 if (!visited.some(([r, c]) => r === seat[0] && c === seat[1])) {
//                     const cost = calDist(seat, visited);
//                     if (cost > dist) {
//                         dist = cost;
//                         next = seat;
//                     } else if (cost === dist) {
//                         if (j < next[1]) {
//                             next = seat;
//                         }
//                     }
//                 }
//             }
//         }
//         answer.push(next);
//         visited.push(next);
//     }

//     return visited;
// }

// function solution(n, k) {
//     const visited = chkSeats(n);
//     return(visited[k - 1]);
// }

function calDist(seat, visited) {
  const [row, col] = seat;
  let minDist = Infinity;
  for (const s of visited) {
    const [allocatedRow, allocatedCol] = s;
    const dist = Math.abs(row - allocatedRow) + Math.abs(col - allocatedCol);
    minDist = Math.min(minDist, dist);
  }
  return minDist;
}

function findNextSeat(n, visited) {
  let minDist = -1;
  let nextSeat = [0, 0];

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      const seat = [i, j];
      if (!visited.some(([r, c]) => r === seat[0] && c === seat[1])) {
        const cost = calDist(seat, visited);
        if (cost > minDist || (cost === minDist && j < nextSeat[1])) {
          minDist = cost;
          nextSeat = seat;
        }
      }
    }
  }
  return nextSeat;
}

function generateVisitedSeats(n) {
  const visited = [[1, 1]];
  for (let i = 1; i < n * n; i++) {
    const nextSeat = findNextSeat(n, visited);
    visited.push(nextSeat);
  }
  return visited;
}

function findSeat(n, k) {
  const visited = generateVisitedSeats(n);
  return visited[k - 1];
}

function solution(n, k) {
  return findSeat(n, k);
}
