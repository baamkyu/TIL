let _ = require('lodash')

// arr.sort()
// 주의! 배열 재정렬 (배열 자체가 변경됨)
let arr = [27, 8, 5, 13];

arr.sort((a, b) => {
  console.log(a, b)
  return a - b
});
// 8 27 5 13
// 5 8 27 13
// 5 8 13 27 순서대로 작동
console.log(arr) // [5, 8, 13, 27]

// 하지만! 이런 복잡한 함수를 사용하기 보다는 Lodash 라이브러리를 사용
_.sortBy(arr)



// 배열의 모든 수 합치기
let arr2 = [1, 2, 3, 4, 5]

// for, for of, forEach

// 1. forEach
let result = 0
arr2.forEach((num) => {
  result += num
})
console.log(result) // 결과 15

// 2. reduce
let arr3 = [1, 2, 3, 4, 5]
// prev = 이전 값, 여태까지의 결과 값
// cur = 현재 값
// 이전 값 + 현재 값 연산을 반복
const result2 = arr3.reduce((prev, cur) => {
  return prev + cur;
}, 0)
// 여기서 0은 초기값, 100으로 바꾸면 115가 출력됨
console.log(result2) // 결과 15



// reduce 사용해서 미성년자 찾기
let userList = [
  { name: "Mike", age: 30},
  { name: "Tom", age: 19},
  { name: "Jane", age: 23},
  { name: "Alex", age: 17},
  { name: "Marry", age: 13},
  { name: "Steve", age: 20},
]

let result3 = userList.reduce((prev, cur) => {
  if (cur.age <= 19) {
    prev.push(cur.name);
  } 
  return prev;
}, [])
console.log(result3) // 결과 ['Tom', 'Alex', 'Marry']

// reduce 사용해서 나이 합
let result_age_sum = userList.reduce((prev, cur) =>{
  return prev += cur.age
}, 0)
console.log(result_age_sum) // 결과 122

// reduce 사용해서 이름이 4글자인 사람의 정보 찾기
let result_namelength_four = userList.reduce((prev, cur) => {
  if (cur.name.length === 4) {
    prev.push(cur)
  }
  return prev;
}, [])
console.log(result_namelength_four)
// 결과
// [
//   { name: 'Mike', age: 30 },
//   { name: 'Jane', age: 23 },
//   { name: 'Alex', age: 17 }
// ]