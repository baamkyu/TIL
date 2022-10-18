// while문
// let으로 해야함. const는 재할당 X
// let i = 0
// while (i<5) {
//   console.log('하이')
//   i++
// }

// 전통적인 for문
const numbers = [1, 2, 3, 4, 5]
// for (변수할당, 종료조건, 증가) {로직}
for (let j=0; j < numbers.length; j++) {console.log(numbers[j])}

// Array용 for -> 요소를 꺼내는 for이며, of문을 쓴다
for (const number of numbers) {
  console.log(number, typeof(number))
}

// Object용 for이며, key를 꺼내는 for이다. in 문을 쓴다
const person = {myName: 'alex', address: 'seoul'} // key값에는 따옴표를 붙여도 안 붙여도 됨
for (const key in person) {console.log(key, person(key))}

// 그런데 이거 배열을 돌아버리면 스트링으로 