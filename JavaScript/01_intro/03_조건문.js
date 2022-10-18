// if, else, else if === truthy, falsy 값에 따라 실행됨.
// if (조건) {로직}
let age = 10
if (age > 19) {
  console.log('성인')
} else if (age > 8) {
  console.log('학생')
} else {
  console.log('유아')
}

// switch & case
const myId = 'manager'

switch (myId) {
  case 'admin':{
      console.log('관리자님 환영합니다!')
      break
    }
  case 'manager': {
      console.log('매니저님 환영합니다!')
      break
    }
  default: {
    console.log(`${myId}님 환영합니다!`)
  }
}
