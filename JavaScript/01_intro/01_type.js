// 데이터 종류 (자료형) -> JS는 데이터 기준으로 사고

/*
Primitive Types
1. Number
2. String
3. Empty (null, undefined)
4. Boolean
*/

// python의 f스트링같은 역할
let myName = 'alex'
let greeting = `Hello, my name is ${myName}`  // 백틱
console.log(greeting)

console.log('안녕' + '하세요')  // 얘도 더해짐
console.log('안녕' + 3 + '살 아가야') // js의 강제 형변환


// Number
console.log(
  'Number types: ',
  Infinity, -Infinity, NaN
)

// Empty Values
console.log(undefined, null)

//Boolean Types -> true, false는 소문자!
console.log(true, false)