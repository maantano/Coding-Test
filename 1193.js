let X = Number(require("fs").readFileSync("/dev/stdin"));
const 오름차순 = [];
const 내림차순 = [];
let groupCounter = 0;
while (X > 0) {
  groupCounter++;
  X -= groupCounter;
}
for (let i = 0; i < groupCounter; i++) {
  오름차순.push(i + 1);
  내림차순.push(groupCounter - i);
}

if (groupCounter % 2 === 0) {
  console.log(
    `${오름차순[X + groupCounter - 1]}/${내림차순[X + groupCounter - 1]}`
  );
} else {
  console.log(
    `${내림차순[X + groupCounter - 1]}/${오름차순[X + groupCounter - 1]}`
  );
}
