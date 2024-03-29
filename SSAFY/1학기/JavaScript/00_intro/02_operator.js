/*
Operands
1. unary (단항 연산자)
-, typeof, ++, --, !

2. binary (이항 연산자)
+, -, *, /, +=, -=, *=, /=, >, >=, <, <=,
&&(and), ||(or)

3. ternary (삼항 연산자)
? :

1. 산술연산자
2. 수 비교연산자
3. 동등/일치 연산자
4. 논리연산자
*/

let i = 1
// i에 대한 평가가 끝난 후, 1을 더한다
console.log(i++)
// i에 대한 평가 전에 1을 더한다.
console.log(++i)

// ! => 이건 오른쪽 애를 평가한 다음 boolean 값을 뒤집어버림
console.log(!true)

// type 확인
console.log(3, typeof 3, typeof(3))

console.log(typeof undefined, typeof null)


// 동등 => 안 씀 (복잡한 형변환 이슈 추후 공부) => google에 js spongebob 검색
0 == '0'  // true
0 == []   // true
'0' == [] // false

// and => &&, or => ||
console.log(true && true && true)

// 가치평가 ? true일 경우 : false일 경우
console.log(1 > 2 ? '크다' : '작다')

let a = 1
const even_or_odd = a % 2 ? 'odd' : 'even'
console.log(even_or_odd)

