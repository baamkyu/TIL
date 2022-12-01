
const numbers = [1, 2, 3, 4, 5]

// // 1.
// const doubleEle = function (number) {
//   return number * 2
// }

// const newArray = numbers.map(doubleEle)

// console.log(newArray)

// // 2.
// const newArray = numbers.map(function {number}{
//   return number * 2
// })
// console.log(newArray)
// 3.
const newArray = numbers.map((number) => {
  return number * 2
})
console.log(newArray)

// // 4.
// const newArray = numbers.map((number) => number * 2)
// console.log(newArray)