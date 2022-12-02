function makeCounter() {
  let num = 0;
  return function() {
    return num++;
  };
}

let counter = makeCounter();

console.log(counter()); // 0
console.log(counter()); // 1
console.log(counter()); // 2

// 위 코드에서 num을 은닉화 하였음.
// num을 임의로 100이든 1000이든 값을 부여할 수 없고,
// counter() 함수만을 통해 조작 가능.