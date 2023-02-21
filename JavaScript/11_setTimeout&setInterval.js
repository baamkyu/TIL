// setTimeout

// 1. 함수 정의해서 실행
function fn(){
	console.log(3)
}
setTimeout(fn, 3000);

// 2. 함수 정의없이 바로 실행
setTimeout(function() {
  console.log(3)
}, 3000)


// setInterval, clearInterval
let num = 0;
function showTime() {
  console.log(`안녕하세요. 접속하신지 ${num++}초가 지났습니다.`)
  if (num > 5) {
    clearInterval(tId)
  }
}
const tId = setInterval(showTime, 1000);