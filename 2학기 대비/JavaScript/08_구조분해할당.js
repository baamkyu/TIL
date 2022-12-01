// 배열구조분해1
let users = ['Mike', 'Tom', 'Jane']
let [userA1, userA2, userA3] = users;
console.log(userA1); // 'Mike'
console.log(userA2); // 'Tom'
console.log(userA3); // 'Jane'

// 배열구조분해2
let str = "Mike-Tom-Jane"
let [userB1, userB2, userB3] = str.split('-');
console.log(userB1); // 'Mike'
console.log(userB2); // 'Tom'
console.log(userB3); // 'Jane'

// 배열구조분해 : 일부 반환값 무시
let [userC1, , userC2] = ['Mike', 'Tom', 'Jane', 'Alex']
console.log(userC1); // 'Mike'
console.log(userC2); // 'Jane'

// 배열구조분해 : 바꿔치기
let a = 1;
let b = 2;
[a, b] = [b, a];

// 객체구조분해
let userD = {name: 'Mike', age: 30}
let {name, age} = userD;
console.log(name); //'Mike'
console.log(age); // 30

// 객체구조분해 : 새로운 변수 이름으로 할당
let userE = {name: 'Mike', age: 30}
let {name: userName, age: userAge} = userE;
console.log(userName); // 'Mike'
console.log(userAge); // 30