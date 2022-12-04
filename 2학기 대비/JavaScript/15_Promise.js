const pr = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('OK')
  }, 1000)
})

pr.then((result) => {
  console.log(result)
}).catch((err) => {
  console.log(err)
}). finally(() => {
  console.log('끝')
});



// 3개의 주문
const f1 = () => {
  return new Promise((res, rej) => {
    setTimeout(() => {
      res("1번 주문 완료")
    }, 1000)
  })
}

const f2 = (message) => {
  console.log(message)
  return new Promise((res, rej) => {
    setTimeout(() => {
      res("2번 주문 완료")
    }, 5000)
  })
}

const f3 = (message) => {
  console.log(message)
  return new Promise((res, rej) => {
    setTimeout(() => {
      res("3번 주문 완료")
    }, 3000)
  })
}

// 실행
console.log('시작')
f1()
  .then(res => f2(res)) // f1이 정상적으로 작동하면 f2실행
  .then(res => f3(res)) // 다음 동작도 정상적으로 작동하면 f3실행
  .then(res => console.log(res)) // 다음 동작도 정상적으로 작동하면 console.log(res)
  .finally(() => {
    console.log("끝")
  }) // 끝날 때 "끝" 출력



// Promise.all()
// 1번 주문 1초, 2번 주문 5초, 3번 주문 3초 걸린다는 가정하에
// 동시에 주문 받을 수 없을까? 할 떄 사용하는 함수
console.time('x') // 시간 재기
Promise.all(([f1(), f2(), f3()]))
  .then((res) => {
    console.log(res)
    console.timeEnd('x')
  })

  // Promise.race : 하나라도 완료되면 끝냄
  console.time('xx') // 시간 재기
  Promise.race(([f1(), f2(), f3()]))
  .then((res) => {
    console.log(res)
    console.timeEnd('xx')
    console.log('race 끝')
  })