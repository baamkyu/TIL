# 공통PJT Learn

## 여러 개의 useState를 관리하는 법

```jsx
function FillPage() {
  const [inputValue, setInputValue] = useState({
    inputId: '',
    inputPw: '',
    inputCheckPw: '', 
    inputNickname: '',
  })

  const { inputId, inputPw, inputCheckPw, inputNickname } = inputValue;

  // Input tag handling
  const handleInput = (e) => {
    const { name, value } = e.target
    setInputValue({
      ...inputValue,
      [name]: value
    })
  }
}
```

<br>
<br>

## 회원가입 시 유용하게 사용되는 유효성 검증

```jsx
const check_num = /[0-9]/; // 숫자 
const check_eng = /[a-zA-Z]/; // 문자 
const check_spc = /[~!@#$%^&*()_+|<>?:{}]/; // 특수문자
const check_pw = /^[a-z|A-Z|0-9|~!@#$%^&*()_+|<>?:{}]+$/ // 숫자, 문자, 특수문자만 사용 가능
const check_nickname = /^[ㄱ-ㅎ|가-힣|a-z|A-Z|0-9|]+$/ // 한글, 영어, 숫자만 사용 가능

// 1. ID 유효성 검사 -> '@' 와 '.' 이 포함되어 있는가?
const isValidId = inputId.includes('@') && inputId.includes('.')

// 1. PW 유효성 검사 -> 8자~12자 사이 / 숫자,문자,특수문자로 이루어져 있고 모두 사용했는가?
const isValidPwLength = inputPw.length>=8 && inputPw.length<=12
const isValidPwForm = check_pw.test(inputPw) && check_num.test(inputPw) && check_eng.test(inputPw) && check_spc.test(inputPw)

// 1. 닉네임 유효성 검사 -> 2자~10자 사이 / 한글, 영어, 숫자로만 이루어져 있는가?
const isValidNicknameLength = inputNickname.length>=2 && inputNickname.length<=10
const isValidNicknameForm = check_nickname.test(inputNickname)

// 2. ID 유효성 검사 로직
const checkId = () => {
  if (isValidId === false){
    setEmailMsg('잘못된 유형의 이메일 주소입니다.')
  }
  else {
    setEmailMsg('사용 가능한 이메일입니다.')
  }
}

// 2. PW 유효성 검사 로직
const checkPw = () => {
  if (isValidPwLength && isValidPwForm){
    setPwMsg('사용 가능한 비밀번호입니다')
  } else {
    setPwMsg('사용할 수 없는 비밀번호입니다')
  }
}

// 2. 비밀번호확인 유효성 검사 로직
const reCheckPw = () => {
  if (inputCheckPw === inputPw) {
    setPwCheckMsg('비밀번호 확인 완료')
  }
}

// 2. 닉네임 유효성 검사 로직
const checkNickname = () => {
  if (isValidNicknameLength && isValidNicknameForm){
    setNicknameMsg('사용 가능한 닉네임입니다')
  } else {
    setNicknameMsg('사용할 수 없는 닉네임입니다')
  }
}
```

<br>
<br>

## true / false에 따른 조건부 CSS

```
<span className={ nicknameCheck ? styles.canuse : styles.cannotuse }>중복확인</span>
```
<br>
<br>

## 삼항 연산자를 이용한 조건부 렌더링
```
{emailCorrect ? <div><button onClick={ mailCheck }>메일로 인증번호 받기</button></div> : null}
```
-> emailCorrect 가 true이면 button 출력, false이면 null 출력

<br>
<br>

## axios API 연결
💡 axios에는 크게 GET, POST 방식이 있는데 세분화 하면 get, delete, post, put 방식이 있다.

get, delete 방식은 query string 형태로 보내줘야 하고
 (ex. `axios.get('/member/check/email?email=' + inputId, {withCredentials : false})` )

post, put 방식은 body 형태로 보내줘야 한다!! 
(ex. `axios.post('/member/check/email', axiosInfo, {withCredentials : false})` )
```
// 아이디 중복 확인 API
  const isSameId = () => {
    if (isValidId) {
      axios.get('/member/check/email?email=' + inputId, {withCredentials : false})
        .then((res) => {
          const { accessToken } = res.data;
          // API 요청하는 콜마다 헤더에 accessToken 담아 보내도록 설정
          axios.defaults.headers.common[
            "Authorization"
          ] = `Bearer ${accessToken}`;
          // accessToken을 localStorage, cookie 등에 저장하지 않는다!
          // console.log("input id: ", inputId)
          // console.log(res)
          // setCanUseId(true)
        })
        .catch((err) => {
          if(err.response.status === false){
            console.log('axios catch');
          }
          console.log("Error occurred : " + err);
        })
      } else {alert('아이디 유효성 확인ㄱㄱ')}
  }
  ```
<br>
<br>

## 상단으로 이동하는 토글 버튼

```
function MoveToTopToggle() {

    /* const MoveToTop = () => {
      // top:0 >> 맨위로  behavior:smooth >> 부드럽게 이동할수 있게 설정하는 속성
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }; */


    const MoveToTop = () => {
      document.getElementById("postlist").scrollIntoView(false, {behavior: 'smooth'});
    };
      

    
    // const postList = document.getElementById("postlist").scrollIntoView(true);
    return (
    <div className={styles.arrowiconposition}>
        <img className={styles.arrowicon} alt='' src={MoveToTopBtn} onClick={MoveToTop}></img>
    </div>
  )
}
```
  내가 원래 알고 있던 코드는 이런 식으로 window의 scroll위치를 top: 0으로 움직이는 로직의 코드였다.
  하지만 이번 프로젝트에서의 구성은 윈도우의 스크롤이 한 페이지로 구성되어 있었고 피드를 나타내는 공간을 차지하는 div 안에 피드 아이템 컴포넌트들이 반복되도록 구현되어 있었다.
  이 때문에 윈도우의 스크롤을 0으로 움직여도 변화가 없었고 그럼 피드아이템의 맨 윗부분으로 스크롤을 이동해야겠다는 생각을 했다.
  그래서 생각을 한 게 피드를 나타내는 공간을 차지하는 div에 id를 부여했고 그 아이디의 최상단을 불러오자라는 로직이었다.
  
  ⭐️ 여기서 의문점 : 
  scrollIntoView의 첫번째 인자를 true로 하면 상단의 위치로 이동하는 함수가 되고 false로 하면 하단의 위치로 이동하는 함수라는 검색 결과가 있었다. 하지만 여기서 true를 하면 애매한 중간 어딘가?로 이동을 하고 false를 넣어보니 해당 div의 최상단으로 잘 이동하게 된다. 왜일까?! -> 아직 해결 못함..
<br>
<br>
## useState의 상태관리가 한 발짝 늦어지는 오류

필터 아이콘 누른 상태에서 첫 번째 정렬(최신순)을 누르면 최신순으로 정렬해야하나 최신순을 누른 후 다른 버튼을 눌렀을 때가 되어서야 최신순으로 정렬이 된다는 문제가 생겼다 ㅜㅜㅜㅜ!!!
```
// 필터 함수
const onFilter = () => {
    setFilterStandard(num)
    if (filterStandard === 1) {
      getPostList().then((response) => {
        setPosts(response.postList) // 작동 됨
        console.log(response.postList)
        console.log(filterStandard)
      }
    )} else if (filterStandard === 2) {
      getPostListByComment().then((response) => {
        setPosts(response.postList) // 작동 됨
        console.log(response.postList)
        console.log(filterStandard)
      })
    } else if (filterStandard === 3) {
      getPostListByWeather(0, 'SUNNY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
    }
    )} else if (filterStandard === 4) {
      getPostListByWeather(0, 'CLOUDY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
      }
    )} else if (filterStandard === 5) {
      getPostListByWeather(0, 'RAINY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
    }
    )}
  }

{/* 필터 아이콘 누른 상태 */}
        {filtering ? (
          <div className={styles.filterselectbox}>
            <div className={styles.filtertextdiv}>
              <span
                className={
                  filterStandard === 1
                    ? styles.filtertextstandard
                    : styles.filtertext
                }
                onClick={() => {
                  onFilter(1);
                }}
              >
                최신순
              </span>
```
`useEffect`를 통해 filterStandard가 변경될 때 onFilter를 실행하도록 설정하니 해결되었다!!
```
// filterStandard가 변경될 때 onFilter 함수를 실행해주는 hook
useEffect(() => {
    onFilter();
  }, [filterStandard])

// 클릭했을 때 filterStandard의 값을 바꿔주는 함수
  const changeFilterStandard = (num) => {
    setFilterStandard(num)
  }

// filterStandard에 따라 유효한 데이터만 필터링하여 정렬해주는 함수
  const onFilter = () => {
    if (filterStandard === 1) {
      getPostList().then((response) => {
        setPosts(response.postList) // 작동 됨
        console.log(response.postList)
        console.log(filterStandard)
      }
    )} else if (filterStandard === 2) {
      getPostListByComment().then((response) => {
        setPosts(response.postList) // 작동 됨
        console.log(response.postList)
        console.log(filterStandard)
      })
    } else if (filterStandard === 3) {
      getPostListByWeather(0, 'SUNNY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
    }
    )} else if (filterStandard === 4) {
      getPostListByWeather(0, 'CLOUDY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
      }
    )} else if (filterStandard === 5) {
      getPostListByWeather(0, 'RAINY').then((response) => {
        setPosts(response);
        console.log(filterStandard)
    }
    )}
  }

// return 부분
{filtering ? (
          <div className={styles.filterselectbox}>
            <div className={styles.filtertextdiv}>
              <span
                className={
                  filterStandard === 1
                    ? styles.filtertextstandard
                    : styles.filtertext
                }
                onClick={() => {
                  changeFilterStandard(1);
                }}
              >
```
<aside>
💡 여태까지 얕은 지식으로 useEffect는 처음 렌더링 될 때 기본으로 띄워주는 hook인 줄 알았는데, 2번째 인자인 [ ] 안에 변수를 넣어주면 해당 변수가 바뀔 때마다 첫번째 인자가 실행되는 hook임을 알게 되었다.

</aside>

<br>
<br>

### true일 때는 false로, false일 때는 true로 바꾸기

```jsx
// 원래 사용하던 방식
const [isValid, setIsValid] = useState(false);

const isValidType = () => {
	if (isValid === false) {
		setIsValid(true)
	} else {
		setIsValid(false)
	}
}

// 더 간단한 방식
const [isValid, setIsValid] = useState(false);
  const isValidType = () => {
    setIsValid((pre) => !pre);
  };
```

<aside>
💡 기존 값의 반대값을 주려는 상황일 때, 한 줄로 사용이 가능하다!
</aside>

<br>
<br>

### axios get요청할 때 한글 인자가 전달이 안 된다 (인코딩 깨짐)
<aside>
💡 해결법 : `npm i iconv-lite`
</aside>

⇒ 찾아보니 백에서 알아서 처리해주는 부분인데 url을 잘못 입력해서 전달이 안 되는 거였음..

### Uncaught TypeError: getNotification().then() is not a function

```jsx
// NotificationAPI.js
const getCheckEmail = (email) => {
  let url = `/api/member/check/email?email=${email}`;
  let value = null;
  axios
    .get(url)
    .then((response) => {
      value = response.data;
    })
    .catch((err) => {
      console.log("이메일 중복 검사 중 에러 발생");
    });
  return value;
};

// NotificationPage.js
const [notiList, setNotiList] = useState([]);

useEffect(() => {
  getNotification().then((res) => {
    setNotiList(res) 
  })
}, [])
```

위 코드에서 실행을 하니 콘솔창에 Uncaught TypeError: ~~~~ .then is not a function 이라는 에러를 만났다. 


```jsx
// NotificationAPI.js
const getNotification = async () => {
  let url = `/api/notification`;
  let value = {};
  await axios
    .get(url)
    .then((response) => {
      value = response.data
      console.dir(value)
    })
    .catch((err) => {
      console.log("알림 가져오는 중 오류 발생");
    });
  return value;
};
```

asnyc await 를 사용하여 오류 탈출!

<aside>
💡 **"TypeError: then is not a function" 오류는 `then()`메소드가 프로미스가 아닌 값에 대해 호출될 때 발생합니다.**

**오류를 해결하려면 메서드를 호출하기 전에 값을 약속으로 변환하거나 `then()`유효한 약속에서만 메서드를 호출해야 합니다.**

</aside>

<br>
<br>

## useRef()를 통해 input태그 focus하기

[React | Input control 과 useRef의 적절한 사용 (+ Input 유효성 검사)](https://velog.io/@imzzuu/React-Input-control-%EA%B3%BC-useRef%EC%9D%98-%EC%A0%81%EC%A0%88%ED%95%9C-%EC%82%AC%EC%9A%A9-Input-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%82%AC)

```jsx
function CheckSignUp() {
	const onFocus = useRef([]);
	if (!verifyedId) {
      alert('사용할 아이디 입력 후 인증을 완료해주세요.')
      onFocus.current[0].focus(); // onFocus 배열의 첫번째 값을 focus()
    } else if (!pwMsgColor) {
      alert('사용 가능하지 않은 비밀번호입니다.')
      onFocus.current[1].focus();
    } else if (!pwCheckMsgColor) {
      alert('동일한 비밀번호를 입력해주세요.')
      onFocus.current[2].focus();
    } else if (!nicknameMsgColor) {
      alert('사용할 수 없는 닉네임입니다.')
      onFocus.current[3].focus();
    } else if (!useCheck) {
      alert('필수 약관을 동의해주세요.')
    } else if (!canUseNickname) {
      alert('이미 사용중인 닉네임입니다.')
      onFocus.current[3].focus();
    } else if (verifyedId && pwMsgColor && pwCheckMsgColor && nicknameMsgColor && useCheck && canUseNickname) {
      axios.post('api/member/sign-up', axiosInfo, {withCredentials: false})
      .then ((res) => {
        alert('회원가입 성공')
        navigate('/main', { state: res.data })
      })
      .catch((err) => {
        console.log(err)
      })
    }
}

return (
	<div>
    <p>아이디</p>
      <input ...
            ref={(el) => (onFocus.current[0] = el)}/>
    <p>비밀번호</p>
      <input ...
            ref={(el) => (onFocus.current[1] = el)}/>
    ...
    </div>

)
```