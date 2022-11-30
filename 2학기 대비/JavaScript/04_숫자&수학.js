// 숫자 -> 문자열로 변환
let num = 10;
num.toString(); // "10"
num.toString(2); // "1010"

let num2 = 255;
num2.toString(16); // "ff" 


// 수학
let userRate = 30.1234;

// 문제 요구사항 : 소수점 둘째자리까지 표현

Math.round(userRate * 100)/100 // 30.12
userRate.toFixed(2); // "30.12"
Number(userRate.toFixed(2)); // 30.12

userRate.toFixed(0); // "30"
userRate.toFixed(6); // "30.123400"