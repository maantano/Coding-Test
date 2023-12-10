// function solution(n, sequence) {
//   let answer = 0;

//   if (sequence[0] !== 1) {
//     // sequence[0]이 1이 아닌 경우, 해당 집에서부터 1번 집까지의 거리를 더함
//     const diff = Math.abs(sequence[0] - 1);
//     answer += Math.min(diff, n - diff);
//   }

//   for (let i = 0; i < sequence.length - 1; i++) {
//     const diff = Math.abs(sequence[i] - sequence[i + 1]);
//     answer += Math.min(diff, n - diff);
//   }

//   return answer;
// }

// // 예시 1
// const n1 = 5;
// const sequence1 = [1, 2, 3, 4, 5];
// const result1 = solution(n1, sequence1);
// console.log(result1); // 출력값: 4

// // 예시 2
// const n2 = 5;
// const sequence2 = [3, 5, 4, 1, 2];
// const result2 = solution(n2, sequence2);
// console.log(result2); // 출력값: 8

// ================
// let card = ["AAAKKKKKMMMMM", "ABCDKJ"];
// let arr = [
//   ["A", "A", "A", "K", "K", "K", "K", "K", "M", "M", "M", "M", "M"],
//   ["A", "B", "C", "D", "K", "J"],
// ];

let card = ["GPQM", "GPMZ", "EFU", "MMNA"];
let arr = [
  ["A", "B", "A", "C", "D", "E", "F", "G"],
  ["N", "O", "P", "Q", "R", "S", "T", "U"],
  ["H", "I", "J", "K", "L", "K", "M", "M"],
];
let answer = [];
let d = {};

for (let i = 0; i < card.length; i++) {
  for (let j = 0; j < card[i].length; j++) {
    if (!d[j]) {
      d[j] = 1;
    } else {
      d[j] += 1;
    }
  }
}

function chkWord(word) {
  let visited = Array.from({ length: word.length }, () =>
    Array(arr.length).fill(0)
  );
  let visitedRow = new Array(arr.length).fill(0);

  for (let i = 0; i < word.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (d[i] < 1) {
        break;
      }
      if (arr[j].includes(word[i])) {
        visited[j][i] = 1;
        visitedRow[j] = 1;
        d[i] -= 1;
        continue;
      }
    }
  }

  if (visited.flat().includes(0) || visitedRow.includes(0)) {
    return;
  }

  answer.push(word);
}

for (let i of card) {
  chkWord(i);
}

if (!answer.length) {
  console.log(["-1"]);
} else {
  console.log(answer);
}
