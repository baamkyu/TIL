// 이 부분을 bmw, benz, audi에 상속
const car = {
  wheels: 4,
  drive() {
    console.log("drive..");
  }
}

// 원래는 주석 해제한 코드로 작성해야하지만
// 공통적인 속성들은 car라는 속성을 이용해 상속시켜줌
const bmw = {
  color: "red",
  // wheels: 4,
  navigation: 1,
  // drive() {
  //   console.log("drive..");
  // }
}

const benz = {
  color: "black",
  // wheels: 4,
  // drive() {
  //   console.log("drive..");
  // }
}

const audi = {
  color: "blue",
  // wheels: 4,
  // drive() {
  //   console.log("drive..");
  // }
}

// car를 bmw에 상속시킴
bmw.__proto__ = car;


const x5 = {
  color: "white",
  name: "x5",
}

// bmw를 x5에 상속시킴 (x5 < bmw < car)
x5.__proto__ = bmw;



// 객체가 가지고 있는 property 찾기
for (p in x5) {
  if (x5.hasOwnProperty(p)) {
    console.log('o', p);
  } else {
    console.log('x', p);
  }
}