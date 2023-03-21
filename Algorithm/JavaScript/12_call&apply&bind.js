let _ = require('lodash')

const mike = {
  name: "Mike",
}

const tom = {
  name: "Tom",
}

function showThisName() {
  console.log(this.name);
}

// call
showThisName(); // undefined
showThisName.call(mike); // Mike
showThisName.call(tom); // Tom

// update > call -> lodash 사용
function update(birthYear, job) {
  this.birthYear = birthYear;
  this.job = job;
}
update.call(mike, 1999, "singer");
console.log(mike)

// update > apply -> 매개변수를 배열로 받음

update.apply(tom, [2002, "teacher"]);
console.log(tom)



// 배열의 최소값, 최대값 찾기
// 1. 스프레드 연산자 이용
const nums = [3, 10, 1, 6, 4];
const minNum = Math.min(...nums)
const maxNum = Math.max(...nums)

console.log(minNum)
console.log(maxNum)

// 2. apply 이용 -> 매개변수를 배열로 받음
const minNum_apply = Math.min.apply(null, nums);
//  = Math.min.apply(null, [3, 10, 1, 6, 4])
const maxNum_apply = Math.max.apply(null, nums);

console.log(minNum_apply)
console.log(maxNum_apply)

// 3. call 이용 -> 매개변수를 순서대로 직접 받음
const minNum_call = Math.min.call(null, ...nums);
const maxNum_call = Math.max.call(null, ...nums);

console.log(minNum_call)
console.log(maxNum_call)


// bind
const user = {
  name: "Mike",
  showName: function() {
    console.log(`hello, ${this.name}입니다.`)
  },
}

user.showName();

let fn = user.showName;

// fn.call(user);
// fn.apply(user);

let boundFn = fn.bind(user);
boundFn();