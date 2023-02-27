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

### 1.2 조금 더 복잡한 자료형 - Array, Object

### Array

```tsx
let hobbies: string[];
hobbies = ['Sports', 'Cooking', 25]
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

# 3. 함수

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