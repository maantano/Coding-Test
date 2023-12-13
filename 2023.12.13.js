// // 달리기 경주 ####################################################################################
// // let players = ["mumu", "soe", "poe", "kai", "mine"];
// // let callings = ["kai", "kai", "mine", "mine"];
// // let results = ["mumu", "kai", "mine", "soe", "poe"];

// // # 실패
// // function solution(players, callings) {
// //   for (let i = 0; i < callings.length; i++) {
// //     let idx = players.indexOf(callings[i]);
// //     let item = players.splice(idx - 1, 1, players[idx]);
// //     players.splice(idx, 1, item[0]);
// //   }
// //   return players;
// // }
// // function solution(players, callings) {
// //   const playerMap = {};
// //   for (let i = 0; i < players.length; i++) {
// //     playerMap[players[i]] = i;
// //   }

// //   for (let i = 0; i < callings.length; i++) {
// //     const idx = playerMap[callings[i]];
// //     const tmp = players[idx - 1];

// //     players[idx - 1] = callings[i];
// //     players[idx] = tmp;

// //     playerMap[callings[i]] -= 1;
// //     playerMap[tmp] += 1;
// //   }
// //   return players;
// // }
// // solution(players, callings);

// // // 추억 점수 ####################################################################################
// // name = ["may", "kein", "kain", "radi"];
// // yearning = [5, 10, 1, 3];
// // photo = [
// //   ["may", "kein", "kain", "radi"],
// //   ["may", "kein", "brin", "deny"],
// //   ["kon", "kain", "may", "coni"],
// // ];
// // result = [19, 15, 6];
// // function solution(name, yearning, photo) {
// //   var answer = [];
// //   const score = {};
// //   for (let i = 0; i < name.length; i++) {
// //     score[name[i]] = yearning[i];
// //   }

// //   for (let i = 0; i < photo.length; i++) {
// //     let tmp = 0;
// //     photo[i].forEach((el) => {
// //       if (score[el]) tmp += score[el];
// //     });
// //     answer.push(tmp);
// //   }
// //   return answer;
// // }

// // solution(name, yearning, photo);

// // #븡대감기 ####################################################################################

// bandage = [5, 1, 5];
// health = 30;
// attacks = [
//   [2, 10],
//   [9, 15],
//   [10, 5],
//   [11, 5],
// ];
// result = 5;

// bandage = [3, 2, 7];
// health = 20;
// attacks = [
//   [1, 15],
//   [5, 16],
//   [8, 6],
// ];

// function solution(bandage, health, attacks) {
// let ing = 0;
// let attkidx = 0;
// let answer = health;
// for (let i = 0; i <= attacks[attacks.length - 1][0]; i++) {
// 	if (i == attacks[attkidx][0]) {
// 	ing = 0;
// 	answer -= attacks[attkidx][1];
// 	attkidx++;
// 	} else {
// 	if (answer < health) {
// 		answer++;
// 	}
// 	}
// 	if (answer <= 0) return -1;
// 	if (ing != 0 && ing == bandage[0]) {
// 	answer += bandage[2];
// 	ing = 0;
// 	}
// }
// return answer;
// }
// console.log(solution(bandage, health, attacks));

// function solution(bandage, health, attacks) {
//   const maxHealth = health;
//   const [t, x, y] = bandage;

//   let lastAttackTime = 0;

//   for (const [attackTime, damage] of attacks) {
//     const timeDiff = attackTime - lastAttackTime - 1;
//     const heal = timeDiff * x + Math.floor(timeDiff / t) * y;
//     health = Math.min(health + heal, maxHealth);
//     health -= damage;
//     if (health <= 0) return -1;
//     lastAttackTime = attackTime;
//   }
//   return health;
// }

// solution(bandage, health, attacks);

// #공원 산책 ####################################################################################

// park = ["SOO", "OOO", "OOO"];
// routes = ["E 2", "S 2", "W 1"];
// result = [2, 1];

// function solution(park, routes) {
//   const N = park.length;
//   const M = park[0].length;

//   // 시작 좌표 설정
//   let start;
//   for (let i = 0; i < N; i++) {
//     for (let j = 0; j < M; j++) {
//       if (park[i][j] == "S") start = [i, j];
//     }
//   }
//   // 방향 객체
//   const directions = {
//     E: [0, 1],
//     W: [0, -1],
//     S: [1, 0],
//     N: [-1, 0],
//   };
//   // 주어진 이동정보 배열에 담기
//   for (const route of routes) {
//     const [dir, distanceStr] = route.split(" ");
//     let distance = parseInt(distanceStr);
//     let [nx, ny] = start;
//     // 주어진 걸음수 만큼 한칸씩 이동
//     let step = 0;
//     while (step < distance) {
//       nx += directions[dir][0];
//       ny += directions[dir][1];
//       // 만약 밖에 나가게 되거나 X를 만나게 된다면 종료
//       if (nx < 0 || N <= nx || ny < 0 || M <= ny || park[nx][ny] === "X") break;
//       step++;
//     }
//     // 원하는 걸음수를 채우면 start는 마지막 위치로 바꿈
//     if (step === distance) start = [nx, ny];
//   }

//   return start;
// }

// class Deque {
//   constructor() {
//     this.arr = 0;
//     this.head = 0;
//     this.tail = 0;
//   }
//   push_front(item) {
//     if (this.arr[0]) {
//       for (let i = this.arr.length; i > 0; i--) {
//         this.arr[i] = this.arr[i - 1];
//       }
//     }
//     this.arr[this.head] = item;
//     this.tail++;
//   }
//   push_back(item) {
//     this.arr[this.taill++] = item;
//   }
//   pop_front(item) {
//     if (this.head >= this.tail) {
//       return null;
//     } else {
//       const result = this.arr[this.hae++];
//       return result;
//     }
//   }
//   pop_back(item) {
//     if (this.head >= this.tail) {
//       return null;
//     } else {
//       const result = this.arr[--this.tail];
//       return result;
//     }
//   }
// }

// solution(park, routes);

// #바탕화면 정리 ####################################################################################
// wallpaper = [
//   "..........",
//   ".....#....",
//   "......##..",
//   "...##.....",
//   "....#.....",
// ];
// wallpaper = [".#...", "..#..", "...#."];
// wallpaper = [
//   ".##...##.",
//   "#..#.#..#",
//   "#...#...#",
//   ".#.....#.",
//   "..#...#..",
//   "...#.#...",
//   "....#....",
// ];

// wallpaper = ["..", "#."];

// result = [0, 1, 3, 4];
// #실패
// function solution(wallpaper) {
//   var answer = [];
//   let minX = 50;
//   let minY = 50;
//   let maxX = -1;
//   let maxY = -1;
//   wallpaper.forEach((paper, idx) => {
//     if (paper.indexOf("#") >= 0 && minX > paper.indexOf("#")) {
//       minX = idx;
//     }
//     paper.split("").forEach((el, idx) => {
//       if (el === "#" && idx < minY) minY = idx;
//     });
//     if (paper.indexOf("#") >= 0 && maxX < paper.indexOf("#")) {
//       maxX = idx;
//     }
//     paper.split("").forEach((el, idx) => {
//       if (el === "#" && idx > maxY) maxY = idx;
//     });
//   });
//   return [minX, minY, maxX + 1, maxY + 1];
// }
// solution(wallpaper);

// function solution(wallpaper) {
//   const X = [];
//   const Y = [];
//   for (let i = 0; i < wallpaper.length; i++) {
//     for (let j = 0; j < wallpaper[i].length; j++) {
//       if (wallpaper[i][j] === "#") {
//         Y.push(i);
//         X.push(j);
//       }
//     }
//   }

//   X.sort((a, b) => a - b);
//   Y.sort((a, b) => a - b);
//   return [Y[0], X[0], Y[Y.length - 1] + 1, X[X.length - 1] + 1];
// }
// solution(wallpaper);

// #덧칠하기 ####################################################################################

// n = 8;
// m = 4;
// section = [2, 3, 6];
// result = 2;
// n = 5;
// m = 4;
// section = [1, 3];
// n = 4;
// m = 1;
// section = [1, 2, 3, 4];

// function solution(n, m, section) {
//   let paint = section[0];
//   answer = 1;
//   for (let i = 1; i < section.length; i++) {
//     if (section[i] - paint >= m) {
//       answer++;
//       paint = section[i];
//     }
//   }
//   console.log(answer);
//   return answer;
// }

// solution(n, m, section);

// #대충 만든 자판 ####################################################################################

// keymap = ["ABACD", "BCEFD"];
// targets = ["ABCD", "AABB"];
// keymap = ["AA"];
// targets = ["B"];
// result = [9, 4];
// function solution(keymap, targets) {
//   let keyDic = {};
//   let answer = [];
//   for (let i = 0; i < keymap.length; i++) {
//     keymap[i].split("").forEach((el, idx) => {
//       if (el in keyDic) {
//         if (keyDic[el] > idx) keyDic[el] = idx + 1;
//       } else {
//         keyDic[el] = idx + 1;
//       }
//     });
//   }
//   for (let i = 0; i < targets.length; i++) {
//     let tmp = 0;
//     targets[i].split("").forEach((el, idx) => {
//       if (el in keyDic) tmp += keyDic[el];
//       else tmp -= 1;
//     });
//     if (tmp) answer.push(tmp);
//   }
//   if (answer.length) return answer;
//   else return [-1];
// }
// solution(keymap, targets);

// function solution(keymap, targets) {
//   const answer = [];
//   const map = new Map();

//   for (const key of keymap) {
//     for (let i = 0; i < key.length; i++) {
//       if (!map.has(key[i]) || i + 1 < map.get(key[i])) map.set(key[i], i + 1);
//     }
//   }

//   for (const target of targets) {
//     let count = 0;
//     for (let i = 0; i < target.length; i++) {
//       count += map.get(target[i]);
//     }
//     answer.push(count || -1);
//   }

//   return answer;
// }

// #카드 뭉치 ####################################################################################

// cards1 = ["i", "drink", "water"];
// cards2 = ["want", "to"];
// goal = ["i", "want", "to", "drink", "water"];
// result = "Yes";

cards1 = ["i", "water", "drink"];
cards2 = ["want", "to"];
goal = ["i", "want", "to", "drink", "water"];
// result = "Yes";
// function solution(cards1, cards2, goal) {
//   let c1 = cards1.shift();
//   let c2 = cards2.shift();
//   let c3 = goal.shift();
//   if (
//     cards1.length + cards2.length < goal.length ||
//     cards1.length + cards2.length > goal.length
//   )
//     return "No";
//   while (cards1.length > 0 || cards2.length > 0) {
//     if (c1 === c3) {
//       c1 = cards1.shift();
//       c3 = goal.shift();
//     } else if (c2 === c3) {
//       c2 = cards2.shift();
//       c3 = goal.shift();
//     } else {
//       return "No";
//     }
//   }
//   return "Yes";
// }
// console.log(solution(cards1, cards2));

function checkCards(cards, goal) {
  const cardsFilteredByGoal = goal.filter((item, index) =>
    cards.includes(item)
  );
  const cardFilteredByIndex = cardsFilteredByGoal.filter(
    (item, index) => item === cards[index]
  );
  if (cardFilteredByIndex.length !== cardsFilteredByGoal.length) {
    return false;
  }
  return true;
}

function solution(cards1, cards2, goal) {
  if (checkCards(cards1, goal) && checkCards(cards2, goal)) {
    return "Yes";
  }

  return "No";
}
