let cnt = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"];
let card = ["AAAKKKKKMMMMM", "ABCDKJ"];
// let arr = [
//   ["A", "A", "A", "K", "K", "K", "K", "K", "M", "M", "M", "M", "M"],
//   ["A", "B", "C", "D", "K", "J"],
// ];

cnt = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"];
card = ["GPQM", "GPMZ", "EFU", "MMNA"];
// arr = [
//   ["A", "B", "A", "C", "D", "E", "F", "G"],
//   ["N", "O", "P", "Q", "R", "S", "T", "U"],
//   ["H", "I", "J", "K", "L", "K", "M", "M"],
// ];
solution();
function solution() {
  let answer = [];
  let cnt = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"];
  let card = ["AAAKKKKKMMMMM", "ABCDKJ"];
  let arr = cnt.map((str) => str.split(""));
  // let arr = [
  //   ["A", "A", "A", "K", "K", "K", "K", "K", "M", "M", "M", "M", "M"],
  //   ["A", "B", "C", "D", "K", "J"],
  // ];

  cnt = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"];
  card = ["GPQM", "GPMZ", "EFU", "MMNA"];
  // arr = [
  //   ["A", "B", "A", "C", "D", "E", "F", "G"],
  //   ["N", "O", "P", "Q", "R", "S", "T", "U"],
  //   ["H", "I", "J", "K", "L", "K", "M", "M"],
  // ];
  for (let i of card) {
    chkWord(i);
  }

  if (!answer.length) {
    return ["-1"];
  } else {
    return answer;
  }
}

function chkWord(word) {
  let visited = Array.from({ length: card.length }, () =>
    Array(word.length).fill(0)
  );
  let visitedRow = Array(card.length).fill(0);
  let d = {};

  for (let i = 0; i < card.length; i++) {
    for (let j = 0; j < cnt[i].length; j++) {
      if (!(card[i][j] in d)) {
        d[card[i][j]] = 1;
      } else {
        d[card[i][j]] += 1;
      }
    }
  }
  for (let i = 0; i < word.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (!(word[i] in d)) {
        return;
      }

      if (arr[j].includes(word[i])) {
        visited[j][i] = 1;
        visitedRow[j] = 1;
        d[word[i]] -= 1;
        continue;
      }
    }
  }
  let hasNegative = Object.values(d).some((value) => value < 0);
  if (visitedRow.includes(0) || hasNegative) {
    return;
  }
  answer.push(word);
}
// for (let i of card) {
//   chkWord(i);
// }

// if (!answer.length) {
//   return ["-1"];
// } else {
//   return answer;
// }

// function solution(card,word){
//   let answer = [];
//   let arr = card.map((str) => str.split(""));
//   chkWord(word,arr)

//   for (let i of card) {
//     chkWord(i);
//   }

//   if (!answer.length) {
//     return ["-1"];
//   } else {
//     return answer;
//   }

// }

// let card = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"];
// let word = ["AAAKKKKKMMMMM", "ABCDKJ"];
// // let arr = [
// //   ["A", "A", "A", "K", "K", "K", "K", "K", "M", "M", "M", "M", "M"],
// //   ["A", "B", "C", "D", "K", "J"],
// // ];

// card = ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"];
// word = ["GPQM", "GPMZ", "EFU", "MMNA"];
// // arr = [
// //   ["A", "B", "A", "C", "D", "E", "F", "G"],
// //   ["N", "O", "P", "Q", "R", "S", "T", "U"],
// //   ["H", "I", "J", "K", "L", "K", "M", "M"],
// // ];
// let answer = [];
// let arr = card.map((str) => str.split(""));

// function chkWord(word, arr, card) {
//   let visited = Array.from({ length: card.length }, () =>
//     Array(word.length).fill(0)
//   );
//   let visitedRow = Array(card.length).fill(0);
//   let d = {};

//   for (let i = 0; i < card.length; i++) {
//     for (let j = 0; j < card[i].length; j++) {
//       if (!(card[i][j] in d)) {
//         d[card[i][j]] = 1;
//       } else {
//         d[card[i][j]] += 1;
//       }
//     }
//   }
//   for (let i = 0; i < word.length; i++) {
//     for (let j = 0; j < arr.length; j++) {
//       if (!(word[i] in d)) {
//         return;
//       }

//       if (arr[j].includes(word[i])) {
//         visited[j][i] = 1;
//         visitedRow[j] = 1;
//         d[word[i]] -= 1;
//         continue;
//       }
//     }
//   }
//   let hasNegative = Object.values(d).some((value) => value < 0);
//   if (visitedRow.includes(0) || hasNegative) {
//     return;
//   }
//   answer.push(word);
// }
// // for (let i of card) {
// //   chkWord(i);
// // }

// // if (!answer.length) {
// //   return ["-1"];
// // } else {
// //   return answer;
// // }

// function solution(card, word) {
//   let answer = [];
//   let arr = card.map((str) => str.split(""));
//   chkWord(word, arr);

//   for (let i of card) {
//     chkWord(i);
//   }

//   if (!answer.length) {
//     return ["-1"];
//   } else {
//     return answer;
//   }
// }
// solution(card, word);
