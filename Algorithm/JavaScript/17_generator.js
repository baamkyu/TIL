// // 함수 중간에 yield 를 멈춤 포인트로 인식하고 next로 실행시켜줌
// function* fn() {
//   try {
//     console.log(1);
//     yield 1;
//     console.log(2);
//     yield 2;
//     console.log(3);
//     console.log(4);
//     yield 3;
//     return "finish";
//   } catch (err) {
//     console.log(err);
//   }
// }
// const a = fn();
// a.next() // 1
// a.next() // 2
// a.next() // 3 4


// // 배열 반복 -> 실행할 때 윗쪽 코드 주석 처리
// const arr = [1, 2, 3, 4, 5];
// function* fn() {
//   console.log(arr[0])
//   yield 1;
//   console.log(arr[1])
//   console.log(arr[2])
//   yield 2;
//   console.log(arr[3])
//   console.log(arr[4])
//   yield 3;
// }

// const arr_a = fn();
// arr_a.next() // 1
// arr_a.next() // 2 3
// arr_a.next() // 4 5


// // next()에 인수 전달
// function* fn() {
//   const num1 = yield "첫번째 숫자를 입력해주세요";
//   console.log(num1);
  
//   const num2 = yield "첫번째 숫자를 입력해주세요";
//   console.log(num2);

//   return num1 + num2;
// }

// const a2 = fn();
// a2.next(1)
// a2.next(2)


// // 값을 미리 만들어 두지 않음
// function* fn() {
//   let index = 0;
//   while (true) {
//     console.log(index)
//     yield index++
//   }
// }
// const a3 = fn();

// a3.next() // 0
// a3.next() // 1
// a3.next() // 2
// a3.next() // 3


// yield* 이용
function* gen1() {
  yield "w"
  yield "o"
  yield "r"
  yield "l"
  yield "d"
}
function* gen2() {
  yield "Hello,"
  yield* gen1()
  yield "!"
}
console.log(...gen2())