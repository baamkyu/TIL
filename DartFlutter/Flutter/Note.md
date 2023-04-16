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