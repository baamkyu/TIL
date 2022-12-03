// 여태까지 비슷한 객체를 만들기 위해서는 아래와 같이 생성자 함수를 이용했음
const User = function (name, age) {
  this.name = name;
  this.age = age;
  this.showName = function () {
    console.log(this.name);
  }
}

const mike = new User('Mike', 30);


// 아래와 같이 클래스로도 만들 수 있음
// constructor : 객체를 만들어주는 생성자 함수
class User2 {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  showName() {
    console.log(this.name);
  }
}

const tom = new User2('Tom', 19);



// 클래스에서의 상속 -> extends 사용
class Car {
  constructor(color) {
    this.color = color;
    this.wheels = 4;
  }
  drive() {
    console.log('drive..')
  }
  stop() {
    console.log('STOP!')
  }
}

class Bmw extends Car {
  park() {
    console.log("PARK")
  }
}

const z4 = new Bmw('blue');

console.log(z4)