// Symbol은 유일한 식별자를 만들 때 사용 => 유일성 보장
const a = Symbol();
const b = Symbol();

console.log(a===b) // false

// Symbol.for
const id1 = Symbol.for('id');
const id2 = Symbol.for('id');
console.log(id1 === id2); // true


// Symbol 활용 사례
// 다른 개발자가 만들어 놓은 객체
const user = {
  name: "Mike",
  age: 30,
};

// 내가 가져와서 작업
const showName = Symbol('show name');
user[showName] = function () {
  console.log(this.name);
}

user[showName]();

// 사용자가 접속하면 보는 메세지
for (let key in user) {
  console.log(`His ${key} is ${user[key]}.`)
}