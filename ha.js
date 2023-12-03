// // function solution(n, k) {
// //   let currentNumber = n.toString();
// //   let count = 1;

// //   while (parseInt(currentNumber) % k !== 0) {
// //     currentNumber += n.toString();
// //     console.log(parseInt(currentNumber));
// //     console.log(parseFloat(currentNumber));
// //     count++;
// //     if (count > n) {
// //       return -1;
// //     }
// //   }

// //   return count;
// // }

// function solution(n, k) {
//   if (n % k === 0) {
//     return 1; // 이미 나누어 떨어지는 경우, 1번만 반복해도 됨
//   }

//   let count = 1;
//   let temp = n;

//   while (true) {
//     temp = temp * 10 + n; // n을 뒤에 이어붙임
//     count += 1;

//     if (temp % k === 0) {
//       return count;
//     }

//     if (count > k) {
//       return -1; // k번 이상 반복해도 나누어 떨어지지 않음
//     }
//   }
// }

// // 테스트 예

// // 테스트 예시

// // 테스트
// //   console.log(solution(22, 9)); // 출력: 9

// // 테스트
// // console.log(solution(25, 15)); // 출력: 3
// // console.log(solution(22, 9)); // 출력: 9

// // function solution(n, k) {
// //   if (n % k === 0) {
// //     return 1;
// //   }

// //   let currentNumber = BigInt(n);
// //   let count = 1;

// //   while (currentNumber % BigInt(k) !== 0) {
// //     currentNumber = BigInt(currentNumber.toString() + n.toString());
// //     console.log("currentNumber ===>", currentNumber);
// //     console.log("BigInt(k) ===>", BigInt(k));
// //     count++;

// //     if (count > n) {
// //       return -1;
// //     }
// //   }

// //   return count;
// // }

// // 테스트
// // console.log(solution(25, 15)); // 출력: 3
// // console.log(solution(22, 9)); // 출력: 9

// const number =>({age:number});
// const number = (number) => ({
//   age: number,
// });
// console.log(number(3));

const { text, name1 } = {
  text: "1",
  name: "min",
};
console.log(text);
