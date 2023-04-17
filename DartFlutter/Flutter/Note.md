# Flutter

### Flutter를 쓰는 이유

이쁜 앱 레이아웃 만들기, In-app Purchase, 광고달아서 돈벌기, 앱 알림, 서버와 통신해서 DB자료 보여주기, 폰에 있는 사진, 연락처, GPS좌표 꺼내기, PG사 카드 결제 연동 모두 가능하다.

React Native보다 성능이 좋다.

- 요즘 Flutter가 뜨는 이유
    - 스케일업이 쉬운가?
    - 버그찾기 쉬운가?
    - 개발자도구 디버깅도구 잘 되어있는가?
    - 안 되는 기능 없나?
    - 라이브러리 양과 질
    - 꾸준한 업데이트
    
    이를 모두 만족함
    
- Flutter가 쉬운 이유
    - Dart 언어 하나만 알면 끝 (Dart를 사용해서 레이아웃, 스타일, 기능개발 모두 가능)
    - 디자인 못하는 사람에게 좋음 (모두 위젯형태로 되어있어서 갖다 쓰기만 하면 끝)
    - 초보자가 개발해도 완성도 높아보임 (빠른 성능, 조작시 피드백, 화면전환 애니메이션, 이쁜 레이아웃 등)
    - 빠른 시간에 완성도 높은 결과물 가능
- Flutter의 단점
    - 구글 느낌 디자인이 너무 많음
    - 문법이 너무 어려움 (class 등)

### Flutter 개발환경 셋팅

1. Flutter SDK 다운로드
2. Android Studio 설치
3. 환경변수 등록
4. 

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
    

### Flutter에서 앱 디자인은 위젯을 짜집기 하는 방식이다.

### 위젯의 종류

- 글자 위젯
- 이미지 위젯
    - /assets라는 폴더를 만들어서 해당 폴더 내에 넣고 이미지 등록을 따로 해줘야 함.
    - pubspec.yaml 파일(앱 등록할 때 필요한 것들 모아놓은 파일)에
    
    ```dart
    flutter:
    	assets:
    		// assets/ 폴더  안에 있는 파일들을 모두 갖다 쓰겠다 선언
    		- assets/
    ```
    
- 아이콘 위젯
- 박스 위젯

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
			// 글자
      home: Text('안녕')
			// 아이콘
      home: Icon(Icons.star)
			// 이미지 
			// 이미지가 프로젝트 폴더 내에 있어야함 (/assets/파일명) 또한 따로 선언해줘야함
	    home: Image.asset('assets/dog.png')

			// 컨테이너 혹은 박스 (용도는 같음)
			// 50의 단위는 LP라는 단위임 (50LP = 약 1.2cm)
			// 아래의 코드는 어디서부터 50을 차지할지 말을 안 해줘서 전체가 파란색이 됨
			home: Container( width: 50, height: 50, color: Colors.blue )
			home: SizedBox()
			// 아래와 같이 Center를 해주면 가운데에 50x50 박스가 생김
			// Center위젯 안에 child라는 위젯을 넣어준 것임
			home: Center(
				child: Container( width: 50, height: 50, color: Colors.blue )
			)
    );
  }
}
```

`Scaffold` : 앱을 상중하로 나눠줌

- appBar: AppBar() 상단
- body: Container() 중간
- bottomNavigationBar: BottomAppBar() 하단

`mainAxisAlignment` : 메인 축 정렬 (display flex와 유사)

`crossAxisAlignment` : 보조 축 정렬

```
body: Align(
  alignment: Alignment.bottomCenter, // 컨테이너의 정렬 위치
	child: Container(
  width: double.infinity, height: 50, // 가로 최대널이, 높이 50컨테이너 생성
  margin: EdgeInsets.all(20), // 4방향 모두 마진 주는 법
  padding: EdgeInsets.fromLTRB(0, 10, 10, 0), // 원하는 곳만 패딩 주고싶을때 좌상우하
	decoration: BoxDecoration( // 테두리, 박스 색깔 지정
	            border: Border.all(color: Colors.black),
	            color: Colors.blue,
	          ),
  child: Text('sdafsdagsadfsaegwaesdf')
),
```

### TextStyle

color : 글자 색깔

fontSize : 글자 크기

letterSpacing : 글자 간격

backgroundColor : 배경 색

fontWeight: 글자 굵기 (ex. fontWeight: FontWeight.w700) → 100~900까지

```dart
body: SizedBox(
	child: Text('안녕하세요',
		style: TextStyle( color: Color(Colors.red) ),
	),
)

body: SizedBox(
	child: Text('안녕하세요',
		style: TextStyle( color: Color(0xff000000) ), // 000000 Hex 컬러코드 스타일
	),
)

body: SizedBox(
	child: Text('안녕하세요',
		style: TextStyle( color: Color.fromRGBO(r, g, b, opacity) ), // RGB, 투명도 적용
)
```

### Icon 스타일링

color, size 등등

```dart
body: SizedBox(
	child: Icon(Icons.star, color: ㅇㅇㅇ),
)
```

### 버튼 스타일링

두 개의 parameter 필수, child 와 onPressed

TextButton()

IconButton()

ElevatedButton() : 색깔 들어간 버튼

```dart
body: SizedBox(
	child: TextButton(
		child: Text('글자'),
		onPressed: () {},
		style: ButtonStyle( shadow 등 여러가지 스타일있음 확인 ㄱㄱ )
)

body: SizedBox(
	child: ElevaatedButton (
		child: Text('글자'),
		onPressed: () {},
		style: ButtonStyle( shadow 등 여러가지 스타일있음 확인 ㄱㄱ )
)

body: SizedBox(
	child: IconButton(
		icon: Icon(Icons.star),
		onPressed: () {},
		style: ButtonStyle( shadow 등 여러가지 스타일있음 확인 ㄱㄱ )
)
```

### AppBar (헤더)

- title : 앱 이름 쓸 수 있음
- leading: 앱 왼쪽 위에 들어갈 아이콘
- actions : [ Icon(Icons.star) ] → 앱 오른쪽에 넣을 아이콘

### 레이아웃 잘 짜는 법

1. 예시 디자인 준비
2. 예시화면을 쪼개서 구성이 어떻게 되어있는지 네모 그리기
3. 바깥 네모부터 하나하나 위젯으로 만들기
4. 마무리 디자인

### 위젯 만들기

- 커스텀 위젯은 class로 만든다
- class안에 build 라는 함수 만드는 부분
- 변하지 않는 UI들은 벼수 함수로 축약해도 상관없음
- 아무거나 다 커스텀위젯을 만들면 성능 이슈가 생길 수 있음. 따라서, 재사용 많은 UI들만 변수에 삽입

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(),
        body: ShopItem(),
      )
    );
  }
}

// stless 입력 후 class 명 지정 후 코드 작성
// StatelessWidget = 완벽한 위젯 완성품
// StatelessWidget의 변수, 함수를 ShopItem으로 가져간다.
class ShopItem extends StatelessWidget {
  const ShopItem({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      child: Text('안녕'),
    );
  }

	build(context) {
		return SizedBox(
			child: Text('안녕'),
		);
	}
}
```

### ListView

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(),
        body: ListView.builder(
					itemCount: 3, // return 값을 몇 번 반복할 거임?
					itemBuilder: (context, i) { // c = context, i = 반복문이 돌면서 1씩 증가
						// 1. 
						return Text(i) // 이게 itemCount만큼 반복 -> 0, 1, 2 출력

						// 2. 아래의 ListTile이 3번 반복되어 출력됨
						return ListTile(
							leading: Image.asset('profile.png'),
							title: Text('홍길동'),
					)
				}
      )
    );
  }
}

```

### 버튼 눌렀을 때 액션 생성

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({Key? key}) : super(key: key);
	
	var a = 1;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
				floatingActionButton: FloatingActionButton(
					// 버튼의 컨텐츠에서 a를 볼 수 있게 함
					child: Text(a.toString()),
					onPressed: (){
						// 버튼 누르면 여기 로직이 실행됨
						a++;
						print(a);	
					},	
				),
        appBar: AppBar(),
        body: ListView.builder(
					itemCount: 3,
					itemBuilder: (context, i) { 
					// 아래의 ListTile이 3번 반복되어 출력됨
						return ListTile(
							leading: Image.asset('profile.png'),
							title: Text('홍길동'),
					)
				}
      )
    );
  }
}

```

### Stateful 위젯 만들기 (실시간 값이 변경하는 위젯)

재렌더링 하는 법 : state쓰면 state변할 때마다 자동 재렌더링 된다.

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

// // stful 입력 후 탭
// class Test extends StatefulWidget {
//   const Test({Key? key}) : super(key: key);
//
//   @override
//   State<Test> createState() => _TestState();
// }
//
// class _TestState extends State<Test> {
//   @override
//   Widget build(BuildContext context) {
//     return const Placeholder();
//   }
// }
 

class MyApp extends StatefulWidget {
  MyApp({Key? key}) : super(key: key);
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var a = 1; // 자동으로 state가 됨, 값이 변하면 a를 쓰는 위젯이 재렌더링됨

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        floatingActionButton: FloatingActionButton(
          child: Text(a.toString()),
          onPressed: () {
            // 버튼 누르면 여기 로직이 실행됨
            print(a);
            // state값 변경하는 함수
            setState(() {
              a++;
            });
          },
        ),
        appBar: AppBar(),
        body: ListView.builder(
          itemCount: 3,
          itemBuilder: (context, i) {
            // 아래의 ListTile이 3번 반복되어 출력됨
            return ListTile(
              title: const Text('홍길동'),
            );
          },
        ),
      ),
    );
  }
}
```

### Flutter의 for 문

itemBuilder(context, i) {} 를 사용한다.

```dart
class _MyAppState extends State<MyApp> {
  var a = 1; // 자동으로 state가 됨, 값이 변하면 a를 쓰는 위젯이 재렌더링됨
  var name = ['김영숙', '홍길동', '피자집'];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(),
        body: ListView.builder(
          itemCount: 3,
          itemBuilder: (context, i) {
            // 아래의 ListTile이 3번 반복되어 출력됨
            return ListTile(
              title: Text(name[i]),
            );
          },
        ),
      ),
    );
  }
}
```

### 좋아요 버튼 눌렀을 때 좋아요 개수(state값) ++

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  MyApp({Key? key}) : super(key: key);
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var a = 1; // 자동으로 state가 됨, 값이 변하면 a를 쓰는 위젯이 재렌더링됨
  var name = ['김영숙', '홍길동', '피자집'];
  var likeCount = [0, 0, 0];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(),
        body: ListView.builder(
          itemCount: 3,
          itemBuilder: (context, i) {
            // 아래의 ListTile이 3번 반복되어 출력됨
            return ListTile(
              leading: Text(likeCount[i].toString()),
              title: Text(name[i]),
              trailing: ElevatedButton(child: Icon(Icons.thumb_up), onPressed: (){
                setState((){
                  likeCount[i]++;
                });
              }),

            );
          },
        ),
      ),
    );
  }
}
```

### Dialog / 모달창