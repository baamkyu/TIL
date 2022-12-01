// 나머지 매개변수 사용
function add(...numbers) {
  let result = 0;
  numbers.forEach((num) => {
    result += num
  })
  console.log(result)
}
add(1, 2, 3);
add(1, 10, 100, 1000, 10000, 100000, 1000000)

// 생성자 함수
function User(name, age, ...skills) {
  this.name = name;
  this.age = age;
  this.skills = skills;
}
const user1 = new User('Mike', 30, 'html', 'css');
const user2 = new User('Tom', 20, 'JS', 'React');
const user3 = new User('Alex', 25, 'English');

console.log(user1);
console.log(user2);
console.log(user3);


// 전개 구문 : 배열
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

let result = [0, ...arr1, ...arr2, 7, 8, 9, 10]
console.log(result) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 원래는 arr.push() / arr.splice() / arr.concat() ... 등을 사용해야하지만
// 나머지 매개변수를 사용하면 손쉽게 해결 가능

// 전개 구문 : 객체
let user = {name: 'Mike'}
let mike = {...user, age: 30}

console.log(mike) // {name: 'Mike', age: 30}


// 전개 구문 : 복제
let arr3 = [1, 2, 3];
let arr4 = [...arr3]; // [1, 2, 3]

let user4 = {name: 'Mike', age: 30};
let user5 = {...user4};

user5.name = 'Tom'

console.log(user4.name); // 'Mike'
console.log(user5.name); // 'Tom'