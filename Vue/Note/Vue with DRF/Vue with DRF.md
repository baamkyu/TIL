# Vue

# 1. Vue with DRF

### Server & Client

- Server는 정보와 서비스를 제공
    - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
    - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답
- Client는 사용자의 정보 요청을 처리, Server에게 응답 받은 정보를 표현
    - Server에게 정보(데이터)를 요청
    - 응답 받은 정보를 가공하여 화면에 표현

### SOP (Same - Origin Policy)

- “동일 출처 정책”
- 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식

![Untitled](Vue%202b347536a1f3435ba3070a349e2bde88/Untitled.png)

![Untitled](Vue%202b347536a1f3435ba3070a349e2bde88/Untitled%201.png)

---

### CORS - 교차 출처 리소스 공유

- “교차 출처 리소스 공유 정책”
- 출처가 달라도 가져올 수 있게 해주는 방법
- 추가 HTTP Header를 사용하여, 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함

### How to set CORS?

`pip install django-cors-header`

`pip freeze > requirements.txt`

## TokenAuthentication 사용 방법

- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
    - 반드시 Token 문자열 함께 삽입
    - 삽입해야 할 문자열은 각 인증 방식마다 다름

`pip install dj-rest-auth`