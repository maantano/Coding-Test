const threeMultiLargest = (arr) => {
  const getCombinations = function (arr, selectNumber) {
    const result = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    arr.forEach((fixed, idx, origin) => {
      const rest = origin.slice(1 + idx);

      const combinations = getCombinations(rest, selectNumber - 1);
      const attached = combinations.map((el) => [fixed, ...el]);
      result.push(...attached);
    });
    return result;
  };

  let answer = [];
  const combi = getCombinations(arr, 3);
  for (let i = 0; i < combi.length; i++) {
    answer.push(combi[i].reduce((acc, cur) => acc * cur, 1));
  }
  console.log(answer);
  console.log(Math.max.apply(null, answer));
  console.log(Math.max(10, 20));
};

a = [1, 2, 3, 4];

threeMultiLargest(a);
