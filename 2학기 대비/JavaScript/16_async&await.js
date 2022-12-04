/* async, await를 사용하면 promise에 메서드를
체인형식으로 생성하는 것보다 가독성이 좋아짐 */

// async, await는 항상 Promise를 반환함
async function getName() {
  return Promise.resolve('Tom')
}
console.log(getName()) 

getName()
  .then((name) => {
    console.log(name) // Tom
  })


// await : async 내부에서 기다렸다가 반환값을 반환해줌
// async 함수 내부에서만 사용 가능
function getName(name) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(name)
    }, 1000)
  })
}

async function showName() {
  const result = await getName('Mike')
  console.log(result)
}

console.log('시작')
showName()


// Promise에서 썼던 내용들을 async, await로 사용 가능함
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
    }, 3000)
  })
}

const f3 = (message) => {
  console.log(message)
  return new Promise((res, rej) => {
    setTimeout(() => {
      res("3번 주문 완료")
    }, 2000)
  })
}

console.log('async, await 시작')
async function order() {
  try {
    const result1 = await f1();
    const result2 = await f2(result1);
    const result3 = await f3(result2);
    console.log(result3)
  } catch(err) {
    console.log(err);
  }
  console.log('async, await 종료')
}
order();