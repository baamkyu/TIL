# Django 과목평가 대비

### 서술형 대비 문제

1. MVC, MTV 패턴

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled.png)

장고는 MVC 패턴을 기반으로 한 MTV 패턴을 사용한다.

- Model
    - 데이터와 관련된 로직을 관리
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
    - MVC패턴에서 Model의 역할
- Templates
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    - MVC패턴에서 View의 역할
- View
    - Model & Template과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리하는 역할
    - MVC패턴에서 Controller의 역할

⇒ 정리 : Django는 MTV 디자인 패턴을 가지고 있음

- Model : 데이터 관련
- Templates : 보여주기 관련
- View : Model & Templates 중간 처리 및 응답 반환

1. 

Project 시작하기 & Settings

> 💡 Django 기본 세팅 명령어들
> 

```python
# 가상환경을 설정합니다.뒤의 venv는 다른 이름으로 설정할 수 있습니다.
# gitignore.io에 가서 python, django, venv를 기입한 후 .gitignore파일 생성 후 복사 + 붙여넣기
$ python -m venv venv
```

```python
# 가상환경을 활성화합니다. 이후 pip list 명령어를 통해 초기화를 확인합니다.
$ source venv/Scripts/activate
```

```python
# 관련 패키지들을 다운받습니다.
$ pip install django==3.2.13
```

```python
# 패키지 설치가 완료된 경우 requirements.txt를 갱신하여 관리합니다.
$ pip freeze > requirements.txt

# 만약 requirements.txt가 있는 경우?
$ pip install -r requirements.txt
```

```python
# 프로젝트를 만들어야 하는 경우 + 현재 디렉토리에 폴더구조 잡기
$ django-admin startproject <프로젝트 명> .
```

```python
# 프로젝트 중간에 참여하는 경우 migrate 진행
# 설계도를 작성합니다.
$ python manage.py makemigrations

# 설계도를 DB에 반영합니다.
$ python manage.py migrate
```

```python
# 프로젝트 시작 명령어 + 현재 위치에서(.) => manage.py가 생기게 됩니다.
$ django-admin startproject <프로젝트명> .
```

```python
# app 생성 => 이후 settings.py의 installed apps에 등록합니다.
# 이 때, trailing comma(,)를 빼먹지 않도록 주의합니다.
$ python manage.py startapp <앱 이름>

```

> 프로젝트 시작 전 유저 대체 먼저하기
> 

```
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

```
# accounts models.py
from django.contrib.auth.models import AbstractUser

# 장고는 시작부터 유저모델을 대체하는 것을 권장하고 있음.
# 나중에 커스텀 할 여지를 남겨두기 위해서 pass로!
class User(AbstractUser):
    pass
```

> Template 구조 잡기 & Namespace
> 

```
# settings.py

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
```

- 이후 최상단(manage.py가 있는곳)에 templates 폴더를 만들고 그 안에 base.html을 생성합니다.
- 상속받을 템플릿들이 들어있는 폴더는 다음과 같이 구조화합니다.

```
<앱 이름>/
    templates/
        <앱 이름>
            상속받을.html
```

3.

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%201.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%202.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%203.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%204.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%205.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%206.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%207.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%208.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%209.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2010.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2011.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2012.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2013.png)

4.

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2014.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2015.png)

5.

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2016.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2017.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2018.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2019.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2020.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2021.png)

ORM

Object - Relational - Mapping

SQL ↔ Django 간의 호환되지 않는 시스템 간에 데이터를 변환해주는 프로그래밍 기술

장점

SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능

객체 지향적 접근으로 인한 높은 생산성

단점

ORM 만으로 완전한 서비스를 구축하기 어려움

ORM 을 사용하는 이유 : 생산성

6.

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2022.png)

- 

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2023.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2024.png)

- redirect

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2025.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2026.png)

![Untitled](Django%20%E1%84%80%E1%85%AA%E1%84%86%E1%85%A9%E1%86%A8%E1%84%91%E1%85%A7%E1%86%BC%E1%84%80%E1%85%A1%20%E1%84%83%E1%85%A2%E1%84%87%E1%85%B5%20910270463b0d4329a26d129a5278b14c/Untitled%2027.png)