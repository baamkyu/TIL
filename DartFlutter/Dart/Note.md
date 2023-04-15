# Dart & Flutter Note

# Dart

### Dart의 장점

UI에 최적화 되어 있다

생산적인 개발환경을 가진다

모든 플랫폼에서 빠르다

### Dart의 원리

Dart는 `Dart Native`와 `Dart Web` 두 가지의 컴파일러를 갖고 있다

`Dart Native` : dart코드를 여러 CPU의 아키텍쳐에 맞게 변환해주는 컴파일러

→ 이를 통해 IOS, Andriod, Windows, Linux, Mac으로 컴파일 가능

`Dart Web` : dart코드를 javascript 코드로 변환해주는 컴파일러

### Dart의 특징

### 1. AOT (Ahead-of-Time)

AOT는 실행 전에 코드를 기계 코드로 컴파일하는 컴파일러 유형인 Ahead-Of-Time의 약자이다.AOT 컴파일러는 일반적으로 해석된 코드에 비해 더 빠르고 더 작은 실행 파일을 생성하지만 **변경 사항이 있을 때마다 코드를 다시 컴파일**해야 하며 컴파일 프로세스가 더 오래 걸릴 수 있다.

iOS, Android, Widows, Mac 등을 위해 컴파일한다는 건 많은 최적화와 기계어로 변환 작성하는 등 많은 작업이 필요로 하기 때문에 시간이 오래 걸린다.

개발모드에서 변경한 코드에 대한 결과를 보고 싶을때마다 처음부터 모든걸 컴파일한다고 하면 개발 경험이 매우 좋지 않다.**이 상황에서는 JIT 컴파일러를 사용해야한다.**

### 2. JIT (Just-In-Time)

JIT는 JIT(Just-In-Time)의 약자로 **미리 코드가 아닌 런타임에 코드를 기계 코드로 컴파일**하는 컴파일러 유형이다. 이를 통해 코드를 보다 효율적으로 실행할 수 있을 뿐만 아니라 최종 실행 파일의 크기도 줄일 수 있다.

JIT 컴파일러는 **dart VM**을 사용하는데 코드의 결과를 바로 화면에 보여준다.JIT 컴파일러는 오직 개발중일 때만 사용한다.따라서 Flutter를 개발할 때 사용하고 있는 **hot-reload**는 JIT 컴파일러 덕분에 가능하다.

### 📌 개발 모드: JIT 컴파일러

### 📌 배포(빌드): AOT 컴파일러

### Variable (변수)

### 1. 변수에 담긴 값을 변경해줄 때는 같은 타입이어야 한다.

```dart
void main() {
	var name = '범규';
	name = 1;   // 오류
	name = 'bk';
}

// 따라서 var 대신 타입 지정을 해줘도 됨
void main() {
	String name = '범규';
	name = 1;   // 오류
	name = 'bk';
}
```

관습적으로 함수 내부에 지역 변수를 선언할 때에는 var를 사용 

그리고 class에서 변수나 property를 선언할 때에는 타입을 지정

### 2. 변수에 담긴 값이 타입을 오가야 할 때는 `Dynamic Type` 을 사용한다

```dart
void main() {
	var name;    // 선언 후 값을 넣지 않으면 dynamic type이 된다.
	name = 1;    // 정상
	name = 'bk'; // 정상
}

void main() {
	dynamic name;
	name = 1;    // 정상
	name = 'bk'; // 정상
}
```

```dart
void main() {
	dynamic name;
	
	// dynamic type인 경우 타입을 모르니 사용할 수 있는 함수가 많이 없다.
	// 따라서 if문을 사용해 문자열인 경우 문자열함수 실행, int인 경우 int형함수 실행과 같이
	// 설정해서 상황에 맞게 사용할 수 있다.
	if (name is String) {
		name.문자열함수()
	}
	if (name is int) {
		name.int형함수()
	}

}
```

### 3. Nullable Variables (null safety)

### 💡데이터를 받아오는 API연결 시에 null safety를 많이 쓴다.

null safety : 개발자가 null 값을 참조할 수 없도록 하는 기능

만약 null을 사용하면 런타임 에러가 뜬다

```dart
// null safety 없이 사용
bool isEmpty(String string) => string.length == 0;

main() {
	isEmpty(null); // 에러
}
```

위의 코드는 String을 보내야 하는 곳에 null 을 보냈기 때문에 NoSuchMethodError 이 뜬다.

아래의 코드는 String타입의 변수에 null이 들어가도 상관 없음을 의미한다.

```dart
void main() {
	String? name = 'bk'; // ?는 해당 변수에 null이 들어가도 됨을 뜻함
	bk = null;           // 정상 작동
	// 1.
	if (name != null) {
		name.isNotEmpty;
	}
	// 2.
	name?.isNotEmpty; // name이 null이 아니라면 isNotEmpty 속성을 달라고 요청
}
```

### 4. Final Variables

보통의 변수는 같은 타입이면 값이 변경이 가능하다. 하지만 값을 변경하지 못하도록 만들 수 있다.

```dart
void main() {
	String name = 'bk';   // 수정 가능
	name = 'bk edit';     // 정상
	final test = 'name';  // 수정 불가능
	test = 'bk';          // 오류
	final String test2 = 'name'; // 타입도 같이 선언 가능 (필수X)
}
```

### 5. Late Variables

### 💡 API와 작업할 때 많이 쓰임

late는 final이나 var 앞에 붙여줄 수 있는 수식어

late는 초기 데이터 없이 변수를 선언할 수 있게 해준다

```dart
void main() {
	late final String name;
	// do something (ex. api호출)
	print(name); // 오류
	name = 'bk';
	print(name); // 정상
}
```

### 6. Constant Variables (Const 변수)

JS의 const는 Dart의 final과 유사하다.

반면에 dart의 const는 compile-time constant를 만들어 준다.

compile-time constant란, final처럼 수정이 안 되는 변수이다.

또한, const는 compile-time에 알고 있는 값이어야 한다. (컴파일 할 때 알고 있는 값이어야 한다)

API에서 받아오는 값 혹은 사용자가 화면에서 입력해야 하는 값이라면 fina / varl을 사용해야함!!!!

```dart
void main() {
	const name = 'bk';
	name = '12'; // 오류 (수정이 불가하기 때문)
}

void main() {
	const API = fetchApi();  // 이것은 compile-time 변수가 아님. 따라서 const 사용 불가
	print(API); // 오류 (컴파일 할 때 알지 못하는 값이기 때문)
}
```

### 변수 선언 정리

1. var 변수
    
    dart의 스타일 가이드에 따르면 웬만한 변수는 var로 사용하는 것을 권장함
    
    ```dart
    void main() {
    	var name = 'bk';
    }
    ```
    

1. var 변수
    
    dart의 스타일 가이드에 따르면 타입을 사용하는 방식은 class의 property를 작성할 때 사용하는 걸 권장함
    
    ```dart
    void main() {
    	int i = 12;
    }
    ```
    

1. final 변수
    
    final은 값을 재할당하지 못하는 변수
    
    ```dart
    void main() {
    	final name = 'bk';
    	name = 'bk2'; //오류, 수정불가
    }
    ```
    

1. dynamic 타입
    
    어떤 데이터 타입이 들어올지 모를 때 사용하는 변수
    
    ```dart
    void main() {
    	dynamic name;
    	if (name is String) {
    		// 문자열 함수 사용
    	}
    }
    ```
    

1. null safety
    
    잘못된 상태의 변수를 참조하는 걸 막아줌
    
    null 값을 참조하지 못하게 해줌
    
    null 이 들어갈 수 있는 경우에 사용하는 변수
    
    ```dart
    void main() {
    	String? name = 'nico';
    	name = null;
    	//1.
    	if (name != null) {
    		name.isEmpty;	
    	}
    
    	//2.
    	name?.isEmpty;
    }
    ```
    
2. late
    
    final, var, String 같은 것들 앞에 써줄 수 있는 수식어
    
    데이터는 나중에 넣고 나중에 변수를 사용하고자 할 때 사용
    
    ```dart
    void main() {
    	late final/var/타입 name;
    	name = '12';
    	print(name); // 12
    }
    ```
    
3. const
    
    컴파일 할 때 값을 이미 알고 있어야 하는 변수 (수정 불가)
    

## #2. Data Types (데이터 타입)

Dart는 거의 모든 자료형과 function이 object로 이루어져 있다.

ex. String bool int double 등

### Lists

Dart에서의 리스트는 collection if와 collection for을 지원한다.

리스트의 마지막은 ‘,’ 로 끝내자. 그러면 자동으로 포매팅 (자동줄바꿈)이 된다.

```dart
void main() {
	// 아래 두 개는 같음 하지만, 웬만하면 var을 쓰자!
	var numbers = [1, 2, 3, 4,];
	List<int> numbers = [1, 2, 3, 4,];
	// 함수들
	numbers.add(1);
	numbers.first;
	numbers.last;
}
```

### collection if

조건에 따라 리스트에 추가할 수 있다.

```dart
void main() {
	// 아래 두 개는 같음 하지만, 웬만하면 var을 쓰자!
	var numbers = [
	1,
	2,
	3,
	4,
	// giveMeFive가 true이면 리스트가 5를 가진다
	if(giveMeFive) 5, 
	];
}
```

### String interpolation

```dart
void main() {
	var name = 'bk';
	var greeting = 'My name is $name';
	print(greeting); // My name is bk 출력

	var age = 20;
	var greeting2 = 'My name is $name, and I\'m ${age + 5} years old';
	print(greeting2) // My name is bk, and I'm 25 years old
}
```

### collection for

```dart
void main() {
	var oldFriends = ['nico', 'lynn'];
	var friends = ['john', 'david', for (var friend in oldFriends) "★ $friend",];
	print(friends) // [john, david, ★nico, ★lynn]
}
```

### Map

Map을 사용해서 key, value의 타입을 지정해줄 수 있다.

Map을 사용하지 않으면 아래와 같다.

```dart
void main() {
	var player = {
// 아래와 같은 경우 Type이 Object로 지정되고, 아무 타입이나 올 수 있다. (like any type in TS)
		'name': 'bk',
		'age': 25.5,
		'super': false,
	}
}
```

Map을 사용해서 타입을 지정해주자.

```dart
void main() {
// key: int형, value: bool형으로 선언해보자
	Map<int, bool> player = {
			1: true,
			2: false,
			3: true
	}
}

// 예제2.
void main() {
// key: int형으로 구성된 리스트, value: bool형으로 선언해보자
	Map<List<int>, bool> player = {
		[1, 2, 3, 5]: true,
	}
}

// 예제3.
void main() {
	List<Map<String, Object>> players = [
		{'name': 'bk', age: 25},
		{'name': 'abc', age: 20},
	]
}
```

Map도 자료형이기 때문에 그에 따른 함수를 갖는다.

이를 확인하려면 Map. 을 쳐서 어떠한 함수가 있는지 확인해봐라!

### Sets

Set은 Python의 Set과 같이 중복을 제거하고 하나의 요소로 받는다.

```dart
void main() {
	// Set 생성 방법 1.
	var numbers = {1, 2, 3, 4};
	// Set 생성 방법 2.
	Set<int> numbers = {1, 2, 3, 4};
	numbers.add(1);
	numbers.add(1);
	numbers.add(2);
	print(numbers); // {1, 2, 3, 4}
}
```

# #3. Functions

### 함수 선언

void 는 아무것도 return 하지 않을 때 사용하는 것이다.

따라서, return 값이 있으면 function을 정의해줘야 한다.

```dart
String sayHello(String name) {
	return "Hello $name";
}

void main() {
	print(sayHello('bk')); // "Hello bk" 프린트
}
```

Dart에서도 작성하고 리턴하고자 하는 코드가 한 줄이라면 간단하게 화살표 함수 가능

```dart
// 예시 1.
String sayHello(String name) => "Hello $name";

void main() {
	print(sayHello('bk'); // "Hello bk" 프린트
}

// 예시 2.
num plus(num a, num b) => a+ b;
```

함수를 하나 만들어보자

```dart
String sayHello(String name, int age, String country) {
	return "Hello $name, age $age, country $country"
}

void main() {
	print(sayHello('bk', 25, 'korea'); // "Hello bk" 프린트
}
```

하지만 ‘bk’, 25, ‘korea’가 무엇을 의미하는지 잘 모를 수 있다.

따라서 named argument라는 것이 존재한다.

함수를 생성할 때, { } 안에 필요한 argument를 입력하고

함수를 사용할 때는 순서를 맞추지 않아도 상관없다.

```dart
String sayHello({String name, int age, String country}) {
	return "Hello $name, age $age, country $country"
}

void main() {
	print(sayHello(
	age: 12,
	country: 'korea',
	name: 'bk'
	)); // "Hello bk" 프린트
}
```

해당 argument에 값을 안 넘겨줄 경우 오류가 난다. 이 경우 두 가지 방법으로 해결할 수 있다.

1. named argument (age, country, name)에 default value를 정하기

```dart
String sayHello({
	String name = 'bk', 
	int age = 25, 
	String country = 'korea'
}) {
	return "Hello $name, age $age, country $country"
}
```

1. required modifier를 이용해서 필수 값으로 만들 수 있다
    
    이러한 경우 반드시 값을 입력해야 한다.
    

```dart
String sayHello({
	required String name, 
	required int age, 
	required String country,
}) {
	return "Hello $name, age $age, country $country"
}
```

Optional Positional Parameters

```dart
String sayHello(
	String name, 
	int age, 
// not required 지정 후 default값을 설정해주면 입력을 하지 않아도 됨
	[String? country = 'korea']) {
	return "Hello $name, age $age, country $country"
}

void main() {
// country를 입력하지 않으면 기본값은 korea가 된다
	sayHello('bk', 25, );
}
```

내 이름을 대문자로 return하기

### Dart에서도 삼항연산자 가능

### QQ operator 라는 기능도 있음

left ?? right ⇒이 연산자에서 left가 null 이면 right를 return한다.

```dart
// 방법 1. 삼항연산자 사용
String capitalizeName(String? name) => name != null ? name.toUpperCase() : 'null';

// 방법 2. ?? 사용
String capitalizeName(String? name) => name.toUpperCase() ?? null;

void main() {
	capitalizeName('bk');
}
```

```dart
// name이 null이면 bk 할당
void main() {
	String? name;
	name ??= 'bk';
}
```