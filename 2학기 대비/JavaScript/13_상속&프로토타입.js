// 1.
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

// 2. 생성자 함수 이용
const car2 = {
  wheels: 4,
  drive() {
    console.log('drive..')
  }
}

// 이렇게 만들어야 color에 들어갈 값을 초기 값에서 바꿀 수 없음
const Bmw = function (color) {
  const c = color;
  this.getColor = function () {
    console.log(c);
    }
  }

Bmw.prototype.wheels = 4;
Bmw.prototype.drive = function () {
  console.log('drive..')
}
Bmw.prototype.navigation = 1;
Bmw.prototype.stop = function () {
  console.log('STOP!!')
}

const x6 = new Bmw('red')
const m4 = new Bmw('blue')

console.log(x6)
console.log(x6 instanceof Bmw)
console.log(x6.constructor === Bmw)