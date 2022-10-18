/*
함수를 정의하는 3가지 방법
1. 선언식
2. 표현식
  2.1. function
  2.2. arrow function
*/

// 1. 선언식
// function 함수이름 () {} === 기명함수
function add(x, y) {
  return x + y
}

let a = add(3, 4)
console.log(a)


// 2. 표현식 === 함수를 변수에 할당해서 정의
// 2.1 function
const sub = function(x, y) {
  return x - y
}

let b = sub(4, 3)
console.log(b)


// 2.2 arrow function (arrow : =>)
// 원래 코드
let cube = function (n) {return n**3}

//arrow function 코드
cube = (n) => {return n**3}

// 인자가 딱 1개라면, () 생략 가능
// {} 안에 return문만 있는 경우 {}와 return 모두 생략 가능
cube = n => n ** 3