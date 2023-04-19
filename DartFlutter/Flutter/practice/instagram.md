# Flutter Instagram Clone

### 초기 세팅

`analysis_options.yaml` 파일에서 ESLint 끄기

```dart
rules:
    prefer_typing_uninitialized_variables: false
    prefer_const_constructors: false
    prefer_const_constructors_in_immutables: false
    avoid_print: false
    prefer_const_literals_to_create_immutables: false메
```

### Appbar 디자인

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(
      MaterialApp(
        theme: ThemeData(
          // 앱 바 색깔 지정
          appBarTheme: AppBarTheme(
            color: Colors.white,
            elevation: 1, // 그림자
            titleTextStyle: TextStyle(color: Colors.black, fontSize: 25),
            actionsIconTheme: IconThemeData(color: Colors.black),
          ),
          // 모든 아이콘들이 보라색으로 적용
          iconTheme: IconThemeData( color: Colors.purple ),
          textTheme: TextTheme(
          ),
        ),
        home: MyApp()
      )
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Instagram'),
        actions: [
          IconButton(
            icon: Icon(Icons.add_box_outlined),
            onPressed: () {},
            iconSize: 24,
          )
        ]
      )
    );
  }
}
```

### theme 디자인 다른 폴더로 빼기

```dart
// lib/style.dart 파일 생성

// 기본 다트 패키지 가져와야함
import 'package:flutter/material.dart';

var theme =  ThemeData(
  // 앱 바 색깔 지정
  appBarTheme: AppBarTheme(
    color: Colors.white,
    elevation: 1, // 그림자
    titleTextStyle: TextStyle(color: Colors.black, fontSize: 25),
    actionsIconTheme: IconThemeData(color: Colors.black),
  ),
  // 모든 아이콘들이 보라색으로 적용
  iconTheme: IconThemeData( color: Colors.purple ),
  textTheme: TextTheme(
  ),
);
```

```dart
// lib/main.dart

import 'package:flutter/material.dart';
// 테마 디자인 코드를 넣은 파일을 import해옴
import './style.dart';

void main() {
  runApp(
      MaterialApp(
        theme: theme,
        home: MyApp()
      )
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Instagram'),
        actions: [
          IconButton(
            icon: Icon(Icons.add_box_outlined),
            onPressed: () {},
            iconSize: 24,
          )
        ]
      )
    );
  }
}
```

하지만 이렇게 import 해서 쓰는 경우, 변수명이 겹치는 경우가 생길 수 있다. 

그런 경우에 사용할 수 있는 방법 2가지

1.  `import './style.dart' as style;` 과 같이 import를 해서 `style.theme`로 사용한다.
2. `style.dart` 파일에서만 사용할 변수는 `var _변수명;` 과 같이 선언을 하면 다른 파일로 import 되지 않는다.

### 동적인 탭 UI를 만들고자 할 때

1. state를 만들어 state에 UI의 현재 상태 저장
2. state에 따라 탭이 어떻게 보일지 작성   ex. state가 0이면 첫째 페이지 보여주기
3. 유저가 쉽게 state 조작할 수 있게 버튼 만들기

```dart
import 'package:flutter/material.dart';
import './style.dart' as style;

void main() {
  runApp(
      MaterialApp(
        theme: style.theme,
        home: MyApp()
      )
  );
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var tab = 0; // 첫째 페이지: 0, 둘째 페이지: 1

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Instagram'),
        actions: [
          IconButton(
            icon: Icon(Icons.add_box_outlined),
            onPressed: () {},
            iconSize: 24,
          )
        ]
      ),
      body: [Text('홈 페이지'), Text('샵 페이지')][tab],
      bottomNavigationBar: BottomNavigationBar(
        // 라벨 적기 싫을 때 적는 코드
        showSelectedLabels: false,
        showUnselectedLabels: false,
        // i는 지금 버튼 누른 버튼의 번호
        onTap: (i){
          setState(() {
            tab = i;
          });
        },
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.home_outlined),
              label: '홈'),
          BottomNavigationBarItem(
              icon: Icon(Icons.shopping_bag_outlined),
              label: '샵'),
        ],
      ),
    );
  }
}
```

### 서버에서 데이터 가져오는 법

- 서버에 GET 요청하면 됩니다
    - GET : 데이터 읽고 싶을 때
    - POST : 데이터 보내고 싶을 때
- URL 기입
- 패키지 설치
    
    ```dart
    // pubspec.yaml 파일에 아래와 같이 입력 후 전구 버튼 누르고 Pub get 눌러 설치
    dependencies:
      flutter:
        sdk: flutter
      http: ^0.13.4
    ```
    
    ```dart
    // 인터넷 사용 허락 받기
    // android/app/src/main/AndroidManifest.xml 파일
    // 첫번째 줄 manifest 아래에 코드 적기
    <uses-permission android:name="android.permission.INTERNET" /> 추가
    ```
    
    ```dart
    // main.dart 에서 import 해오기
    import 'package:http/http.dart' as http;
    import 'dart:convert';
    ```
    
    ```dart
    // GET 요청 보내기
    // 앱 열자마자 겟요청 보내기 -> 최상단쪽에 initState()안에 get요청 코드 작성
    class _MyAppState extends State<MyApp> {
      var tab = 0; // 첫째 페이지: 0, 둘째 페이지: 1
    
    // initState에는 async await를 사용할 수 없기 때문에 따로 함수를 생성해서
    // initState안에 함수를 실행시켜줌
      getData() async {
        var r = await http.get(Uri.parse('https://codingapple1.github.io/app/data.json'));
        var result = jsonDecode(result.body); // JSON형태의 데이터를 Map 타입으로 변환해줌
      }
    
      @override
      void initState() {
        super.initState();
        getData();
      }
    ```
    

### 데이터 실제로 사용하기

1. 데이터는 _MyAppState에서 가져왔음 → Home에서 사용하려면 parameter로 전달해야겠죠?
2. GET요청으로 받아온 데이터는 State로 관리하는 게 좋음
3. 

```dart
import 'package:flutter/material.dart';
import './style.dart' as style;
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(
      MaterialApp(
        theme: style.theme,
        home: MyApp()
      )
  );
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var tab = 0; // 첫째 페이지: 0, 둘째 페이지: 1
  var result = [];

  getData() async {
    var r = await http.get(Uri.parse('https://codingapple1.github.io/app/data.json'));
    setState(() {
      result = jsonDecode(r.body);
      print(result);
    });
  }

  @override
  void initState() {
    super.initState();
    getData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Instagram'),
        actions: [
          IconButton(
            icon: Icon(Icons.add_box_outlined),
            onPressed: () {},
            iconSize: 24,
          )
        ]
      ),
      body: [Home(result: result), Text('샵 페이지')][tab],
      bottomNavigationBar: BottomNavigationBar(
        // 라벨 적기 싫을 때 적는 코드
        showSelectedLabels: false,
        showUnselectedLabels: false,
        // i는 지금 버튼 누른 버튼의 번호
        onTap: (i){
          setState(() {
            tab = i;
          });
        },
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.home_outlined),
              label: '홈'),
          BottomNavigationBarItem(
              icon: Icon(Icons.shopping_bag_outlined),
              label: '샵'),
        ],
      ),
    );
  }
}

class Home extends StatelessWidget {
  const Home({Key? key, required this.result}) : super(key: key);

  final result;

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: result.length, // result 변수의 길이로 itemCount 설정
      itemBuilder: (context, index) {
        // index에 따라 동적으로 아이템 생성
        return ListTile(
          leading: Image.network(result[index]['image']),
          subtitle: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('좋아요 : ${result[index]['likes'].toString()}'),
              Text('글쓴이 : ${result[index]['user'].toString()}'),
              Text('글내용 : ${result[index]['content'].toString()}'),

            ],
          )
        );
      },
    );
  }
}
```

### 데이터를 한번 받아오고 마는 그런 통신할 때 사용하는 방법

`FutureBuilder` : 데이터가 나중에 추가 안되는 경우 유용함

### 무한스크롤 기능

```dart
import 'package:flutter/material.dart';
import './style.dart' as style;
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/rendering.dart'; // 무한스크롤 구현하기 위해 필요한 패키지

void main() {
  runApp(
      MaterialApp(
        theme: style.theme,
        home: MyApp()
      )
  );
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var tab = 0; // 첫째 페이지: 0, 둘째 페이지: 1
  var data = [];

  // GET 요청 성공시 렌더링, 실패시 get요청 실패
  getData() async {
    var d = await http.get(
        Uri.parse('https://codingapple1.github.io/app/data.json'));
    if (d.statusCode == 200) {
      setState(() {
        data = jsonDecode(d.body);
      });
    } else {
      return Text('get요청 실패');
    }
  }

  // 무한스크롤시 데이터 추가하기
  addData(moreData){
    setState((){
      data.add(moreData);
    });
  }

  @override
  void initState() {
    super.initState();
    getData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Instagram'),
        actions: [
          IconButton(
            icon: Icon(Icons.add_box_outlined),
            onPressed: () {},
            iconSize: 24,
          )
        ]
      ),
      body: [Home(data: data, addData: addData), Text('샵 페이지')][tab],
      bottomNavigationBar: BottomNavigationBar(
        // 라벨 적기 싫을 때 적는 코드
        showSelectedLabels: false,
        showUnselectedLabels: false,
        // i는 지금 버튼 누른 버튼의 번호
        onTap: (i){
          setState(() {
            tab = i;
          });
        },
        items: [
          BottomNavigationBarItem(
              icon: Icon(Icons.home_outlined),
              label: '홈'),
          BottomNavigationBarItem(
              icon: Icon(Icons.shopping_bag_outlined),
              label: '샵'),
        ],
      ),
    );
  }
}

class Home extends StatefulWidget {
  const Home({Key? key, required this.data, required this.addData}) : super(key: key);
  final data; // 부모가 보낸건 보통 수정하지 않으므로 final로
  final Function(dynamic) addData;

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  var scroll = ScrollController();

  getMore() async{
    var r = await http.get(Uri.parse('https://codingapple1.github.io/app/more1.json'));
    var moreData = jsonDecode(r.body);
    widget.addData(moreData);
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    // Lister : 왼쪽에 있는 변수(scroll)가 변할 때 마다 안에 있는 로직이 작동
    scroll.addListener(() {
      // print(scroll.position.pixels); // 스크롤의 위치 출려
      // print(scroll.position.maxScrollExtent); // 스크롤을 아래로 내릴 수 있는 영역
      // print(scroll.position.userScrollDirection); // 스크롤 되는 방향
      if (scroll.position.pixels == scroll.position.maxScrollExtent){
        getMore();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
  // 첫 class 안에 있던 변수 사용은 변수명 앞에 widget. 을 붙여야 한다
    if (widget.data.isNotEmpty) {
      return ListView.builder(
        controller: scroll, // 우자기 얼마나 스크롤했는지 정보들이 scroll 변수에 저장됨
        itemCount: widget.data.length, // data 변수의 길이로 itemCount 설정
        itemBuilder: (context, index) {
          // index에 따라 동적으로 아이템 생성
          return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Image.network(widget.data[index]['image']),
                  Text('좋아요 : ${widget.data[index]['likes'].toString()}'),
                  Text('글쓴이 : ${widget.data[index]['user'].toString()}'),
                  Text('글내용 : ${widget.data[index]['content'].toString()}'),
                ],
              );
        },
      );
    } else {
      return Text('데이터 없음');
    }
  }
}
```

### 상세페이지 만들기

아이콘을 누르면 하나의 페이지를 더 띄우는 로직

Upload 위젯을 현재 페이지에 더 띄울 거임 (Navigator.push 사용)