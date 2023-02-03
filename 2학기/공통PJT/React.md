# 공통PJT Learn

여러 개의 useState를 관리하는 법

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

회원가입 시 유용하게 사용되는 유효성 검증

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

true / false에 따른 조건부 CSS

```
<span className={ nicknameCheck ? styles.canuse : styles.cannotuse }>중복확인</span>
```


삼항 연산자를 이용한 조건부 렌더링
```
{emailCorrect ? <div><button onClick={ mailCheck }>메일로 인증번호 받기</button></div> : null}
```
-> emailCorrect 가 true이면 button 출력, false이면 null 출력

### axios API 연결
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
상단으로 이동하는 토글 버튼
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