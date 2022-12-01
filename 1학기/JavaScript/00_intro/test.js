// 주석
/* 여러 줄 주석 */


// // print 대신 쓸 출력함수
// console.log('hi')

// // 알림 띄워주는 함수
// alert('alert 함수가 이걸 띄워줌')



// const alex = {
//   lastName: '권',
//   firstName: '이혁',
//   greeting: function () {
//     return `안녕하세요 ${this.lastName + this.firstName}입니다.`
//   }
// }

// console.log(alex.greeting())



// // forEach
const arr = [1, 2, 3]
// arr.forEach(function (num) {
// 	console.log(num)
// })
// console.log(arr)


// // map
// const arr2 = arr.map(function (num) {
// 	return num*2
// })
// console.log(arr, arr2)


// // map => arrow function
// const arr3 = arr.map(num => num*2)
// console.log(arr, arr3)




// filter 함수
const articles = [
	{pk: 1, title: 'hi'},
	{pk: 2, title: 'hello'},
	{pk: 3, title: 'great'},
]

const hi = articles.filter(article => article.title === 'hi')
console.log(hi)




//
const obj1 = {myName: 'alex', address: 'seoul'}

const obj2 = {number: 3}

const infos = {...obj1, ...obj2}

infos // { myName: 'alex', address: 'seoul', number: 3 }
obj1 // { myName: 'alex', address: 'seoul' }
obj2 // { number: 3 }