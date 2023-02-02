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