# typescript_learn

# 1. 기본형 타입

기본형 타입에는 number, string, boolean, null, undefined, arrays, objects, function types, parameters

### 1.1 주요 기본형 타입 - number, string, boolean

타입스크립트에서 `number`와 `string`은 타입 선언시 소문자로 시작해야하며 대문자로 시작해도 오류가 나지는 않지만 자바스크립트의 Number 혹은 String 객체를 가리키게 된다.

### 타입스크립트에서의 변수 선언

```tsx
// 1. number
let age: number;
age = 25

// 2. number
let age: number = 25

// 3. number - 명시적으로 타입을 표기하지 않아도 초기 선언한 타입을 기억한다
let age = 25

// 4. 오류
let age: number = '25'

// 5. string
let userName: string = 'Max'

// 6. boolean
let isCorrect: boolean = true
```

타입스크립트는 초기에 선언한 변수의 타입과 다른 타입의 값을 할당하면 에러를 나타낸다.

### 1.2 그 외 기본형 타입 - 튜플, void, never, enum, null, undefined

```tsx
// 튜플
let b:[string, number]
b = ['z', 1]
b[0].toLowerCase() // 오류 안 남
b[1].toLowerCase() // 타입 오류

// void
function sayHello():void{
	console.log('hello')
}

// never
function showError():never {
    throw new Error()
}

function infLoop():never{
    while (true) {
        // do something.. never stop
    }
}

// enum - 비슷한 값끼리 묶은 것
// 수동으로 값을 주지 않으면 0부터 숫자로 입력
enum Os {
    Window = 3,
    Ios, // 4
    Android // 5
}

enum Os {
    Window = 3,
    Ios = 10
    Android // 11
}
console.log(Os[10]) // Ios

enum Os {
    Window = 'win',
    Ios = 'ios'
    Android = 'and'
}
console.log(Os['window']) = 'win'

// type을 Os로 지정하면 Os의 값들만 선언해줄 수 있음
let myOs:Os;
myOs = Os.Window

// null, undefined
let a:null = null
let b:undefined = undefined
```

### 1.3 조금 더 복잡한 자료형 - Array, Object

### Array

```tsx
let hobbies: string[];
hobbies = ['Sports', 'Cooking', 25]

let hobbies2: Array<string>
hobbies2 = ['Sports', 'Cooking', 25]
```

### Object

```tsx
let person: {
	name: string;
	age: number;
}

person = {
	name: 'baamkyu',
	age: 25
}

// person에 객체 배열을 저장하고 싶을 때에는 타입 선언 시에 []를 붙여서 배열선언을 해준다.
let person: {
	name: string;
	age: number;
}[]
```

> **참고: 타입 추론**
> 

타입스크립트는 명시적으로 타입을 표기하지 않아도 초기 선언한 타입을 기억한다.

```tsx
let name = 'baamkyu'
name = 123 // 초기 선언한 문자열('baamkyu')과 타입이 달라 에러 발생
```

따라서 명시적으로 적어주는 불필요한 작업 없이 **타입 추론을 사용하는 것이 권장되는 방식**이다.

### Type Aliases

타입스크립트를 사용하다보면 동일한 타입을 반복해서 정의하는 일이 많아진다.

이러한 경우 반복 정의 대신에 `type` 키워드로 Type Aliases(타입 별칭)이라는 걸 만들 수 있다. 

```tsx
// type Aliases를 이용해 한 번의 타입 정의로 여러 번 사용할 수 있다.
type Person = {
  name: string
  age: number
}

const person1: Person = {
  name: '홍길동',
  age: 24
}
```

# 2. 유니온 타입

타입을 정의할 때 `|` 연산자를 사용해 한 개 이상의 타입을 사용할 수 있게 해주는 기능

```tsx
let baamkyu: string | number = 'man'
baamkyu = 25
```

타입 추론을 사용한 경우가 아니라면 타입을 선언해주는 모든 곳에서 사용 가능하다.

# 3. 인터페이스

인터페이스는 상호 간에 정의한 약속 혹은 규칙을 의미한다.

```
// 오류 발생
let user:object;

user = {
    name: 'baamkyu',
    age: 25
}

console.log(user.name)

```

위 코드에서 객체의 key에 접근하려 하면 에러를 발생시킨다.

또한 초기에 문자열로 지정한 `name`을 숫자로 바꿔도 에러 없이 바뀌어 버린다.

이는 각 key의 타입을 지정하지 않았기 때문이다.

따라서, 인터페이스를 이용해 객체, 함수, 클래스 등을 구현하면 초기 지정한 타입을 쉽게 유지할 수 있다.

### 객체 구현

```tsx
interface User {
	name: string
	age: number
}

const myUser: User = {
	name: 'baamkyu',
	age: 25
}

console.log(myUser.name) // baamkyu
myUser.age = 'a' // 타입 에러 발생
```

### 옵셔널 속성

```tsx
interface User {	
	name: string
	age: number
	// ?를 이용해 있어도 되고 없어도 되는 key인 것을 선언해준다
	gender?: string
}

// gender없어도 문제없이 생성
const myUser: User = {
	name: 'baamkyu',
	age: 25
}

// 이후에도 생성 가능
myUser.gender = 'male'
```

### 읽기 전용 속성 (readonly)

```tsx
interface User {
    name: string
    age: number
    gender?: string
		// 변경이 불가능한 key로 선언한다
    readonly birthYear: number
}

let user: User = {
    name: 'baamkyu',
    age: 25,
    birthYear: 1999
}

// 오류 발생
user.birthYear = 2000
```

### 정의하지 않은 속성 사용

```tsx
interface User {
  name: string
  age: number
  // [아무 문자열: key 타입]: value 타입
  [propName: number]: string
  // 모든 타입의 value 저장하기
  // [propName: string]: any
}

const myUser: User = {
  name: 'baamkyu',
  age: 25,
  // number: string 쌍의 요소를 계속 추가 가능
  1: 'A',
  2: 'B'
}
```

### 리터럴 타입 지정

```tsx
type Score = 'A' | 'B' | 'C' | 'D' | 'F'

interface User {
  name: string
  age: number
  [grade: number]: Score
}

const myUser: User = {
  name: 'baamkyu',
  age: 25,
  // number: string 쌍의 요소를 계속 추가 가능
  1: 'A',
  2: 'B'
}
```

### 함수의 정의

```tsx
// 함수1
interface Add {
    (num1: number, num2: number): number;
}

const add : Add = function(x, y) {
    return x + y
}

add (10, 20)

// 함수2
interface IsAdult {
    (age: number): boolean
}

const a:IsAdult = (age) => {
    return age > 19
}

a(25) // true
```

### 클래스 정의

```tsx
interface Car {
  color: string
  wheels: number
  start(): void
}

class Bmw implements Car {
  color
  constructor (c: string) {
    this.color = c
  }
  wheels = 4
  start() {
    console.log('Go')
  }
}

const myCar = new Bmw('red')
console.log(myCar.color) // red
myCar.start() // Go
```

# 4. 함수

### 함수의 정의

- 함수는 인자의 타입과 반환 값의 타입을 정할 수 있다.

```tsx
function add(num1: number, num2: number): number {
	return num1 + num2
}
```

- 아무 것도 반환하지 않을 때는 `void`를 사용한다.

```tsx
function add(num1: number, num2: number): void {
  console.log(num1 + num2)
}
```

### 함수의 인자

- 함수를 호출할 때는 지정한 함수의 인자를 필수로 넘겨주어야 한다.
    
    ```tsx
    function add(num1: number, num2: number): number {
      return num1 + num2
    }
    
    console.log(add(1)) // 에러 발생
    console.log(add(1, 2)) // 3
    console.log(add(1, 2, 3)) // 에러 발생
    ```
    
- 받아도 되고 안 받아도 되는 인자는 `?`를 사용한다.
    
    ```tsx
    function add(num1: number, num2?: number): number {
      return num1 + num2
    }
    console.log(add(1, 2)) // 30
    console.log(add(1, 2, 3)) // 에러 발생
    console.log(add(1)) // NaN (에러 없음)
    ```
    
- 매개변수 여러 타입 지정하기
    
    ```tsx
    function add (num1: number, num2: number | undefined): number {
      if (num2 !== undefined) {
        return num1 + num2
      } else {
        return num1
      }
    }
    
    console.log(add(1, 2)) // 3
    console.log(add(1, undefined)) // 1
    ```
    
- 매개변수 초기화는 ES6 문법과 동일하다
    
    ```tsx
    function add(num1: number, num2 = 10): number {
      return num1 + num2
    }
    
    console.log(add(1, undefined)) // 11
    console.log(add(1)) // 11
    console.log(add(1, 2)) // 3
    ```
    
- Rest 문법이 적용된 매개변수
    
    ```tsx
    function add(...nums: number[]): number {
      return nums.reduce((result, num) => {return result + num}, 0)
    }
    
    console.log(add(1)) // 1
    console.log(add(1, 2, 3, 4)) // 10
    ```
    
- 매개변수를 특정 값으로 지정
    
    ```tsx
    function myFunc (myParam: 1|'a') {
      return myParam
    }
    
    console.log(myFunc(1)) // 1
    console.log(myFunc('a')) // a
    console.log(myFunc(2)) // 에러
    ```
    

# 4. 제네릭 (Generics)

### 제네릭을 사용해야 하는 이유

```tsx
function insertAtBeginning(array: any[], value: any) {
	const newArray = [value, ...array]
	return newArray
}

const demoArray = [1, 2, 3]
const updatedArray = insertAtBeginning(demoArray, -1) // [-1, 1, 2, 3]
```

이러한 경우 타입스크립트는 배열에 숫자만 들어있다는 것을 인식하지 못하기 때문에 updatedArray의 타입은 any[]이다.  그렇다고 해서 문자열배열에 이용할 수도 있으니까 number[] 이라고 선언해줄 수도 없다. 그래서 결국 any[]라고 선언해야하는데 그렇다면 타입스크립트의 지원을 받을 수 없다.

이런 상황을 직면했을 때 제네릭을 사용하면 된다.

### 함수와의 사용

```tsx
// T: 타입파라미터 (주로 T를 사용)
// 전달받은 타입을 어떤 요소에 사용할지 결정
// array와 value의 타입은 같아야 한다고 선언
function insertAtBeginning<T>(array: T[], value: T) {
	const newArray = [value, ...array]
	return newArray
}

const demoArray = [1, 2, 3]
const updatedArray = insertAtBeginning(demoArray, -1) // [-1, 1, 2, 3]
const stringArray = insertAtBeginning([['a', 'b', 'c'], 'd']) // ['a', 'b', 'c', 'd']
```

```tsx
function getSize<T>(arr: T[]): number {
  return arr.length
}

// 각 배열마다 타입을 명시
const arr1 = [1, 2, 3]
console.log(getSize<number>(arr1))

const arr2 = ['a', 'b', 'c']
console.log(getSize<string>(arr2))

const arr3 = [true, false]
console.log(getSize<boolean>(arr3))

// getSize(arr1)과 같이 사용해도 타입 추론에 의해 에러가 나지 않기 때문에 이렇게도 흔히 사용한다.
// 만약 복잡한 코드에서 타입 추정이 되지 않는다면 위와 같이 타입을 명시하는 것이 좋다.
```