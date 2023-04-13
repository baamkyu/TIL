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

# Flutter

### 규칙

- 프로젝트 명은 모두 소문자
- `lib > main.dart` 파일이 메인 페이지
- ESLint Off
    
    ```dart
    # test > analysis_options.yaml
    rules:
    	prefer_typing_uninitialized_variables : false
    	prefer_const_constructors_in_immutables : false
    	prefer_const_constructors : false
    	avoid_print : false
    ```
    
- 메인페이지 코딩 시작 전
    
    ```dart
    # void main() 만 냅두고 나머지 다 지움
    # stless 입력 후 클래스(?)명 입력
    
    ```