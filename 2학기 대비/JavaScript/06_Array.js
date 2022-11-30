// splice() 사용

// 특정 요소 지우기
let arr = [1, 2, 3, 4, 5]
arr.splice(1, 3)
console.log(arr) // [1, 5]

// 특정 요소 지우고 추가
let arr2 = [1, 2, 3, 4, 5]
arr2.splice(1, 3, 100, 200);
console.log(arr2) // [1, 100, 200, 5]

// 지우지 않고 추가
let arr3 = ["나는", "철수", "입니다"];
arr3.splice(1, 0, "대한민국", "소방관");
console.log(arr3) // ["나는", "대한민국", "소방관", "철수", "입니다"]

// 삭제된 요소 반환
let arr4 = [1, 2, 3, 4, 5];
let result = arr4.splice(1, 2);
console.log(result) // [2, 3]
console.log(arr4) // [1, 4, 5]


// arr.slice(n, m) : n부터 m-1까지 반환
// 배열이 초기화 되지는 않음
let arr5 = [1, 2, 3, 4, 5];
arr5.slice(1, 4) // 배열이 초기화 되지는 않음
console.log(arr5) // [1, 2, 3, 4, 5]
console.log(arr5.slice(1, 4)) // [2, 3, 4]

// arr.concat(arr2, arr3, ...) : 합쳐서 새 배열 반환
// 배열이 초기화 되지는 않음
let arr6 = [1, 2];
let arr7 = [3, 4, 5];
arr6.concat(arr7); // 배열이 초기화 되지는 않음
console.log(arr6) // [1, 2] 
console.log(arr6.concat(arr7)) // [1, 2, 3, 4, 5]


// arr.forEach(fn) : 배열 반복
let users = ['Mike', 'Tom', 'Jane'];
// 보통 item 혹은 index 둘 중 한 가지 인자만 사용함
users.forEach((item, index, arr) => {
  console.log(`${index+1}번째 사람은 ${item}입니다.`)
})

// arr.indexOf / arr.lastIndexOf
// 첫번째 인자는 찾는 값, 두번째 인자는 시작 위치를 의미
let arr8 = [1, 2, 3, 4, 5, 1, 2, 3];
arr8.indexOf(3); // 2
arr8.indexOf(3, 3) // 7 -> 3번 인덱스부터 3을 찾아라
arr8.lastIndexOf(3); // 7

// arr.includes() : 포함하는지 확인
let arr9 = [1, 2, 3];
arr.includes(2); // true
arr.includes(8); // false

// arr.find(fn) / arr.findIndex(fn)
// arr.find -> 첫번째 true값만 반환하고 끝, 만약 없으면 undefined를 반환
// arr.findIndex -> 첫번째 true값만 반환하고 끝, 만약 없으면 -1을 반환
let arr10 = [1, 2, 3, 4, 5];
const result2 = arr10.find((item) => {
  return item % 2 === 0;
});

console.log(result2)

// find 사용해서 미성년자 찾기 -> 첫번째만 반환
let userList = [
  { name: "Mike", age: 30},
  { name: "Jane", age: 27},
  { name: "Tom", age: 18},
  { name: "Alex", age: 13},
];
const result3 = userList.find((user) => {
  if (user.age < 19) {
    return true;
  }
  return false;
})
console.log(result3)

// findIndex 사용해서 미성년자 찾기 -> 첫번째만 반환
const result4 = userList.findIndex((user) => {
  if (user.age < 19) {
    return true;
  }
  return false;
})
console.log(result4)


// arr.filter(fn) -> 만족하는 모든 요소를 배열로 반환
const result5 = userList.filter((user) => {
  if (user.age < 19) {
    return true;
  }
  return false;
})
console.log(result5)



// arr.reverse() : 역순으로 재정렬

// 중요!!
// arr.map(fn) : 함수를 받아 특정 기능을 시행하고 새로운 배열을 반환
let userList2 = [
  { name: "Mike", age: 30},
  { name: "Jane", age: 27},
  { name: "Tom", age: 18},
  { name: "Alex", age: 13},
];

let newUserList = userList2.map((user, index) => {
  return Object.assign({}, user, {
    id : index + 1,
    isAdult : user. age > 19,
  })
})
console.log(newUserList)

// join
let arr11 = ["안녕", "나는", "철수야"]
let result6 = arr11.join();     // 안녕,나는,철수야
let result7 = arr11.join("-");  // 안녕-나는-철수야
let result8 = arr11.join(" ");  // 안녕 나는 철수야

// split
const users2 = "Mike,Jane,Tom,Alex"
const result9 = users2.split(",");
console.log(result9) // [ 'Mike', 'Jane', 'Tom', 'Alex' ]

// Array.isArray() : 배열인지 확인
let user2 = {
  name: "Mike",
  age: 30,
}
let userList3 = ["Mike", "Tom", "Jane"];

console.log(typeof user2); // object
console.log(typeof userList3); // object
console.log(Array.isArray(user2)) // false
console.log(Array.isArray(userList3)) // true
