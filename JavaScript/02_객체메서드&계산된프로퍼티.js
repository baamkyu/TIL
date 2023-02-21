// 2. 객체 메서드(Object methods), 계산된 프로퍼티(Computed property)
let n = "name";
let a = "age";

// 예제 1.
const user = {
  [n]: "Mike",
  [a]: 30,
  [1 + 4]: 5, // 계산식도 가능
}
console.log(user)

// 예제 2.
function makeObj(key, val){
  return {
    [key]: val
  }
}

const obj = makeObj('나이', 33);
console.log(obj)



// 복사
const human = {
  name: 'Mike',
  age: 30,
};

// 복제 후 수정
const human2 = Object.assign({}, human);
human2.name = "Tom";

console.log(human)
console.log(human2);

// 키 값만 반환 => Object.keys
const result_keys = Object.keys(human);
console.log(result_keys)
// value 값만 반환 => Object.values
const result_values = Object.values(human);
console.log(result_values)
// 둘 다 반환 => Object.entries
const result_entries = Object.entries(human);
console.log(result_entries)

// entries 반대로
let arr = [
  ["mon", "월"],
  ["tue", "화"],
];

const result_fromEntires = Object.fromEntries(arr);
console.log(result_fromEntires)