## 기초적인 기능들
- CREATE
- READ
- UPDATE
- DELETE

CRUD 기능을 컨트롤 하기 위한 component `Control.jsx` 생성

### CREATE 기능 설명
```
1. 생성하기 누르면 form이 뜨고 해당 form에 title, desc입력하면 리스트에 추가

2. 해당 기능을 수행하려면 현재까지 생성된 리스트의 개수를 세주면서 추가된 데이터에 max_id + 1해서 id값을 만들어줌

3. CREATE하기 위해 버튼을 누르면 상태를 CREATE_PROCESS로 변경 -> 해당 상태에서 동작해야 할 로직 입력,
데이터 입력 후 생성하기 버튼을 누르면 상태를 CREATE로 변경 -> 해당 상태에서 동작해야 할 로직 입력
```

### READ 기능 설명
```
1. for문을 돌면서 클릭한 내용의 id값과 동일한 데이터를 Nav부분에 출력해줌
```

### UPDATE 기능 설명
```
1. UPDATE버튼을 누르면 해당 데이터의 값들이 기본 값으로 입력되어 있어야 함

2. onChange를 이용해 target data의 값을 bind해줌 -> title, desc 각각 해줘야 함
```

### DELETE 기능 설명
```
1. onClick을 이용해 클릭 시 mode를 DELETE_PROCESS로 변경

2. store.js에서 if (mode === 'DELETE_PROCESS') {return false}를 이용해 안 보이게 해줌
```

# 이번 공부를 통해 느낀 점
bind의 원리를 조금이나마 이해할 수 있게 되었고 mode, type을 이용해 상태관리를 할 수 있게 된 것 같다.

생소한 것들이 많아 기본적인 CRUD에도 애를 먹었으나 다소 친해진 것 같다(?)

# 이번 공부를 하면서 어려웠던 점
redux devtools를 설치하고 활용하며 공부하고 있었는데 갑자기 그 기능이 사라져서 google검색으로 시간을 많이 날렸는데 결국은 재부팅하니 다시 생겼다..

배열을 복사한다는 개념 자체가 아직은 생소해서 어떨 때 사용해야하는지 정확히 이해하진 못했다 아마도(?)