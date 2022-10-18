// 변수 설정법
// 1. dash-case(kebab-case) => html, css 사용
// 2. snake_case
// 3. camelCase === lowerCamelCase (JS 주로 활용)
// 4. PascalCase === UpperCamelCase (JS class 명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안 될 것 같은 상수들

// JS 변수에는 var, let, const 형식이 있다.
// 옛날에 사용하던 변수 : var, 최근에 사용하는 변수 : let, const

// let은 재할당 가능, 재선언 불가능
let x = 1;
x = 2;
console.log(x);

let x = 7;
console.log(x);

// const는 재할당 불가능, 재선언 불가능 -> API키, ko-kr 등에 쓰임
const y = 1;
y = 2;
console.log(y);

const y = 3;
console.log(y);

// var는 재할당 가능, 재선언 가능 -> 옛날에 사용하던 변수
var z = 3;
z = 5;
console.log(z)

var z = 10;
console.log(z)

