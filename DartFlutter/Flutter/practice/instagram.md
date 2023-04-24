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


### 폰에 있는 사진 가져오기

아이폰은 따로 설정을 해줘야함

```dart
// ios/Runner/Info.plist
<dict>
	<key>NSPhotoLibraryUsageDescription</key>
	<string>사진첩좀 써도 됩니까</string>
	<key>NSCameraUsageDescription</key>
	<string>카메라 써도 됩니까</string>
	<key>NSMicrophoneUsageDescription</key>
	<string>마이크 권한좀요</string>
```

사진 가져올 폴더에 import 해주기

```dart
import 'package:image_picker/image_picker.dart';
import 'dart:io';
```

사진 필터 적용 가능 → 패키지 설치해야함 `photofilters`

[photofilters | Flutter Package](https://pub.dev/packages/photofilters)

글작성하는 UI 작성

- 주의할 점
    - Image.network()에는 http부터 시작하는 이미지만 가능함
    - 하지만, 유저가 선택한 이미지는 _File 타입임
    - 해결방법 : 이미지가 String타입이면 `Image.network()` 사용, String타입이 아니면 `Image.file()` 사용
- 글 작성 로직
    - State에 데이터를 추가해줌

```dart
import 'package:flutter/material.dart';
import './style.dart' as style;
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/rendering.dart'; // 무한스크롤 구현하기 위해 필요한 패키지
import 'package:image_picker/image_picker.dart';
import 'dart:io';

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
  var userImg;
  var userContent;

  // 게시글 리스트에 게시물 추가하기
  addMyData(){
    var myData = {
      'id': data.length,
      'image': userImg, // 사용자가 설정한 사진
      'likes': 5,
      'date': 'July 25',
      'content': userContent, // 사용자가 작성한 글 내용
      'liked': false,
      'user': 'John Kim'
    };
    setState(() {
      data.insert(0, myData);
    });
  }

  setUserContent(content){
    setState(() {
      userContent = content;
    });
  }

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
            onPressed: () async{
              var picker = ImagePicker();
              // var image = await picker.pickMultiImage(); // 앨범 띄워서 사진 여러장 고르기
              var image = await picker.pickImage(source: ImageSource.gallery); // 앨범 띄워서 사진 한장 고르기
              // var image = await picker.pickImage(source: ImageSource.camera); // 카메라 띄우기
              if (image != null){
                setState((){
                  userImg = File(image.path);
                });
              }

              Navigator.push(context,
                MaterialPageRoute(builder: (c) => Upload(
                  userImg: userImg,
                  setUserContent: setUserContent,
                  addMyData: addMyData,))
              );
            },
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

class Upload extends StatelessWidget {
  const Upload({Key? key, this.userImg, this.setUserContent, this.addMyData}) : super(key: key);
  final userImg;
  final setUserContent;
  final addMyData;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar( actions: [
        IconButton(onPressed: (){
          addMyData();
        }, icon: Icon(Icons.send))
      ]),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Image.file(userImg),
          TextField(onChanged: (String content){
            setUserContent(content);
          },),
          IconButton(
              onPressed: (){
                Navigator.pop(context);
              },
              icon: Icon(Icons.close))
        ]
      )
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
                  widget.data[index]['image'].runtimeType == String
                      ? Image.network(widget.data[index]['image'])
                      : Image.file(widget.data[index]['image']),
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

하지만 State로 데이터를 관리하는 경우, 사용자가 앱을 껐다 키면 초기화된다.

### 데이터 보존방법

1. 서버로 보내서 DB에 저장
2. 폰 메모리카드에 저장 (shared preferences 이용) → 데이터 삭제, 캐시 삭제 누르지 않으면 보관

<aside>
💡 중요한 건 DB에 보관, 덜 중요한 건 shared preferences에 보관

</aside>

### shared preferences

1. 패키지 다운로드

해당 코드 입력 후 Pub get

```dart
// pubspec.yaml
dependencies:
	// ...
	shared_preferences: ^2.0.11
```

1. import

```dart
// main.dart
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
```

1. 저장하고 싶은 데이터 함수 실행

```dart
class _MyAppState extends State<MyApp> {
	...
	saveData() async {
	    var storage = await SharedPreferences.getInstance(); // 저장공간 오픈하는 법
	    storage.setString('name', 'john'); // key, value 형태로 저장
	    var result = storage.getString('name'); // john
	    print(result);
	  }

	@override
  void initState() {
    super.initState();
    saveData(); // 위의 함수가 실행되면서 john 출력
  }
};
```

위는 데이터를 저장하는 방법이다. 그럼 데이터 삭제하는 방법은?

```dart
class _MyAppState extends State<MyApp> {
	...
	saveData() async {
	    var storage = await SharedPreferences.getInstance(); // 저장공간 오픈하는 법
	    storage.setString('name', 'john'); // key, value 형태로 저장
	    var result = storage.remove('name'); // john
	    print(result);
	  }

	@override
  void initState() {
    super.initState();
    saveData(); // 위의 함수가 실행되면서 john 출력
  }
};
```

1. map자료를 저장하고 싶으면?
    
    JSON 형태로 변환해서 저장하자!
    

```dart
class _MyAppState extends State<MyApp> {
	...
	saveData() async {
	    var storage = await SharedPreferences.getInstance(); // 저장공간 오픈하는 법
	    var map = {'age': 20}; // map 형태의 자료
			storage.setString('map', jsonEncode(map)); // key, value 형태로 저장
	    var result = storage.getString('map') ?? 'null'; // null 체크 후 {'age': 20} 출력
	    print(resut) // {'age': 20}
			print(jsonDecode(result)['age']); // 20 -> 반드시 null 체크 해야함!
	  }

	@override
  void initState() {
    super.initState();
    saveData(); // 위의 함수가 실행되면서 john 출력
  }
};
```

<aside>
💡 Shared Preferences 활용해서 인스타처럼 이미 본 게시물은 위에 표시하기

</aside>

GET요청으로 게시글을 조회함

수신완료한 게시물은 변수에 담아둔다

해당 변수를 shared preferences 사용해서 저장해둔다

앱을 다시 키면 shared preferences에 있는 게시물을 맨 위로 가져올 수 있음

⇒ 장점 : 봤던 게시물은 빠르게 로드되고, 서버와 주고받는 데이터 양을 줄일 수 있음!

⇒ 이미지는 저장할 수 없기 때문에 캐싱을 이용한다.

`cached_network_image` 라는 패키지 사용

### 페이지 전환 애니메이션

1. MaterialPageRoute
    
    쉬우나 커스텀의 한계가 있음
    
    ```dart
    class _HomeState extends State<Home> {
    	...
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
    	                  widget.data[index]['image'].runtimeType == String
    	                      ? Image.network(widget.data[index]['image'])
    	                      : Image.file(widget.data[index]['image']),
    	
    	                  // 누르면 프로필로 이동, 페이지전환 애니메이션 작동
    	                  GestureDetector(
                        child: Text(widget.data[index]['user']),
                        onTap: (){
                          Navigator.push(context,
                            // 페이지 트랜지션
    												// 1. 기본
                            MaterialPageRoute(builder: (c) => Profile())
    												// 2. 아이폰 스타일 (오른쪽에서 왼쪽으로 슬라이드되어서 들어옴)
    												CupertinoPageRoute(builder: (c) => Profile())
                          );
                        },
                      ),
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
    };
    
    class Profile extends StatelessWidget {
      const Profile({Key? key}) : super(key: key);
    
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(),
          body: Text('프로필페이지'),
        );
      }
    ```
    
2. PageRouteBuilder
    
    transitionsBuilder: () ⇒ 애니메이션용위젯();
    
    - 애니메이션용 위젯 종류
    
    `FadeTransition()` 
    
    `PositionedTransition()` : 포지션 변경하는 트랜지션
    
    `ScaleTransition()` : 사이즈 줄였다 키웠다
    
    `RotationTransition()` : 회전 트랜지션
    
    `SlideTransition()` : 슬라이드 트랜지션
    
    `Hero()` : 기존에 있던게 커지는 효과
    

아래는 글 작성자의 닉네임을 클릭시 프로필로 이동하는 로직인데, 페이지 전환시 작동하는 애니메이션에 대해 다룬 코드이다.

```dart
class _HomeState extends State<Home> {
	...
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
	                  widget.data[index]['image'].runtimeType == String
	                      ? Image.network(widget.data[index]['image'])
	                      : Image.file(widget.data[index]['image']),
	
	                  // 누르면 프로필로 이동, 페이지전환 애니메이션 작동
	                  GestureDetector(
	                    child: Text(widget.data[index]['user']),
	                    onTap: (){
	                      Navigator.push(context,
	
	                        // 아이폰디자인, import해야함, 오른쪽에서 왼쪽으로 덮어쓰기
	                        // CupertinoPageRoute(builder: (c) => Profile())
	
	                        // 페이지 트랜지션
	                        PageRouteBuilder(
	                            pageBuilder: (c, a1, a2) => Profile(),
	                            // 1.
	                            transitionsBuilder: (c, a1, a2, child) =>
	                                FadeTransition(opacity: a1, child: child)
	                            // 2. 왼쪽에서 들어오는 애니메이션 Offset의 첫번째: x좌표, 두번째: y좌표
	                            // transitionsBuilder: (c, a1, a2, child) =>
	                            //   SlideTransition(
	                            //     position: Tween(
	                            //       begin: Offset(-1.0, 0.0),
	                            //       end: Offset(0.0, 0.0),
	                            //     ).animate(a1),
	                            //     child: child,
	                            //   )
	                        )
	                        // MaterialPageRoute(builder: (c) => Profile())
	                      );
	                    },

	                    // onDoubleTap: (){}, // 더블클릭시 작동
	                    // onHorizontalDragStart: (){}, // 스와이프 했을 때 작동
	                    // onLongPress: (){}, // 길게 눌렀을 때 작동
	                    // onScaleStart: (){}, // 확대했을 때 작동
	                  ),
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
};

class Profile extends StatelessWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Text('프로필페이지'),
    );
  }
```

### State를 3-step으로 보내기 싫으면 Provider 사용

기존에 다른 클래스의 State를 사용하기 위해서는 (ex. Myapp()의 State를 Home()클래스의 자식인 Profile()에서 사용하려면)

Myapp() → Home() → Profile() 순서대로 State를 내려줘야 한다.

커스텀위젯이 많아질수록 state전송이 힘들고 코드가 복잡해진다.

이런 경우, Provider 사용하면 해결!

### Provider란?

클래스 안에서 State를 선언하는 것이 아닌 따로 State보관함(Provider)을 만들어 State를 관리한다.

### Provider 사용법

1. 패키지 코드 작성 후 Pub get

```dart
// pubspec.yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^0.13.4
  image_picker: ^0.8.4+4
  shared_preferences: ^2.0.11
  provider: ^6.0.1
```

1. import

```dart
// 프로젝트 파일
import 'package:provider/provider.dart';
```

1. Store 생성

```dart
class Store1 extends ChangeNotifier {
  var name = 'john kim';
}
```

1. MaterialApp을 감싸준다

```dart
void main() {
  runApp(
    ChangeNotifierProvider(create: (c) => Store1(),
      child: MaterialApp(
        theme: style.theme,
        home: MyApp()
      ),
    )
  );
}
```

1. 사용
    
    Profile 클래스에서 AppBar의 title에 나타내보자
    

```dart
class Profile extends StatelessWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
				// Provider 사용법
        title: Text(context.watch<Store1>().name),
      ),
      body: Text('프로필페이지'),
    );
  }
}
```

### Provider에서 관리하는 State 변경하는 법

1. Provider에 state 변경함수 만들기
    
    변경함수 작동 후 바로 재렌더링 하려면 `notifyListers()` 
    

```dart
class Store1 extends ChangeNotifier {
  var name = 'john kim';
  changeName(){
    name = 'john park';
    notifyListeners(); // 함수 실행되면 재랜더링
  }
}
```

2. 함수 사용

```dart
class Profile extends StatelessWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(context.watch<Store1>().name),
      ),
      body: Column(
        children: [
          ElevatedButton(onPressed: (){

						// 여기서는 context.read로 사용!!
            context.read<Store1>().changeName();

          }, child: Text('버튼'),)
        ]
      )
    );
  }
}
```

### 팔로우 상태 확인해서 팔로우중이 아니면 +1, 팔로우중이면 -1 해보자

1. Store에 함수 만들기

```dart
class Store1 extends ChangeNotifier {
  var name = 'john kim';
  var followNum = 0;
  var isFollowing = false;

  // 팔로우중이 아니면 팔로우+1, 팔로우 중임을 기록
  // 팔로우중이면 팔로우-1, 팔로우 중이 아님을 기록
  clickedFollow() {
    if (isFollowing == false){
      followNum += 1;
      isFollowing = true;
    } else if(isFollowing == true){
      followNum -= 1;
      isFollowing = false;
    }
    notifyListeners();
  }
}
```

1. 함수 사용하기

```dart
class Profile extends StatelessWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(context.watch<Store1>().name),
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          CircleAvatar(
            radius: 30,
            backgroundColor: Colors.grey,
          ),
          Text('팔로워 ${context.watch<Store1>().followNum}명'),
          ElevatedButton(onPressed: (){
            context.read<Store1>().clickedFollow();
          }, child: context.watch<Store1>().isFollowing == false
              ? Text('팔로우')
              : Text('언팔로우')),
        ]
      )
    );
  }
}
```

### Store 여러개 사용하고 싶다면?

1. `ChangeNotifierProvider`이 아닌 `MultiProvider` 사용

```dart
void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (c) => Store1()),
        ChangeNotifierProvider(create: (c) => Store2()),
      ],
      child: MaterialApp(
        theme: style.theme,
        home: MyApp()
      ),
    )
  );
}
```

### 프로필 페이지 방문시 GET요청해서 데이터 가져오고 State에 데이터 담으려면?

1. Store에 데이터 담을 변수 생성 후 데이터 담기
2. **`jsonDecode`** 함수를 사용하여 **`r.body`**에 해당하는 JSON 데이터를 Dart의 **`Map`** 객체로 변환합니다.
3. 변환된 **`Map`** 객체에서 **`result['profileImage']`** 값을 가져와 **`profileImage`** 변수에 할당합니다. 이때 **`cast<String>()`** 메서드를 사용하여 **`result['profileImage']`**가 **`List<dynamic>`** 타입이었을 경우에 문자열(**`String`**) 타입의 리스트로 형변환을 수행합니다.

```dart
class Store1 extends ChangeNotifier {
  var followNum = 0;
  var isFollowing = false;
	var ProfileImage = [];

	getData() async{
    var r = await http.get(Uri.parse('https://codingapple1.github.io/app/profile.json'));

    // JSON데이터를 Map으로 변환
		var result = jsonDecode(r.body);

		// Map에서 result['profileImage']를 가져와 List<dynamic>타입을 String타입의 리스트로 변환
    profileImage = result['profileImage'].cast<String>();

    notifyListeners();
  }

	// ...
}
```

1. Store의 데이터 가져와 렌더링 (GridView UI 포함)

```dart
class Profile extends StatefulWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  State<Profile> createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  @override
  Widget build(BuildContext context) {
    List<String> profileImages = context.watch<Store1>().profileImage
        .map((dynamic imageUrl) => imageUrl as String).toList();
    return Scaffold(
      appBar: AppBar(
        title: Text(context.watch<Store2>().name),
      ),
      body: Column(
        children: [
          SizedBox(height: 16), // 상단 간격 조절
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly, // 가로 정렬
            children: [
              CircleAvatar(
                radius: 30,
                backgroundColor: Colors.grey,
              ),
              Text('팔로워 ${context.watch<Store1>().followNum}명'),
              ElevatedButton(
                onPressed: () {
                  context.read<Store1>().clickedFollow();
                },
                child: context.watch<Store1>().isFollowing == false
                    ? Text('팔로우')
                    : Text('언팔로우'),
              ),
            ],
          ),
          SizedBox(height: 16), // Text와 GridView 사이의 간격 조절
          Expanded(
            child: GridView.builder(
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 3, // 한 줄에 3개의 사진
                mainAxisSpacing: 8, // 사진들 사이의 간격
                crossAxisSpacing: 8, // 사진들 사이의 간격
              ),
              itemCount: profileImages.length,
              itemBuilder: (context, index) {
                return Image.network(
                  profileImages[index],
                  width: 100,
                  height: 100,
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
```

### 앱 사용자에게 알림 보내기

1. 패키지 설치

```dart
// pubspec.yaml
```

2. 알림 셋팅 코드 작성
    
    설정 코드가 기므로 하나의 파일 생성해서 작성하는 것을 권장! `notification.dart` 생성
    

```dart
// notification.dart
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

final notifications = FlutterLocalNotificationsPlugin();

//1. 앱로드시 실행할 기본설정
initNotification() async {

  //안드로이드용 아이콘파일 이름
	// png 파일로 흰색 아이콘스럽게 올려야함 (배경없어야함!)
  var androidSetting = AndroidInitializationSettings('app_icon');

  //ios에서 앱 로드시 유저에게 권한요청하려면
  var iosSetting = IOSInitializationSettings(
    requestAlertPermission: true,
    requestBadgePermission: true,
    requestSoundPermission: true,
  );

  var initializationSettings = InitializationSettings(
      android: androidSetting,
      iOS: iosSetting
  );
  await notifications.initialize(
    initializationSettings,
    //알림 누를때 함수실행하고 싶으면
    //onSelectNotification: 함수명추가
  );
}
```

3. `main.dart`에서 `notification.dart` import 후 앱 처음 실행할 때 알림 받을 수 있게 하기

```dart
// main.dart
import './notification.dart';

// MyApp의 initState에서 initNotification 함수 작동하게 하기 (앱 키자마자 작동)
@override
  void initState() {
    super.initState();
		// ...
    initNotification();
  }
```

4. 알림에 사용할 app_icon 파일을 디렉토리에 추가한다
    
    디텍토리 위치 : `android/app/main/res/drawable/app_icon.png`