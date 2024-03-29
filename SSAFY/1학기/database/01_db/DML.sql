CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
  );

SELECT * FROM users;

SELECT first_name, age FROM users;

SELECT rowid, first_name FROM users;

-- NULL은 가장 작은 값으로 인식 !

-- SELECT : 중복 O
-- SELECT DISTINCT : 중복 X

-- DISTINCT 옵션 사용하면 NULL값은 중복으로 인식

-- 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users
ORDER BY age ASC;

-- 이름과 나이를 나이가 많은 순서대로 조회
SELECT first_name, age FROM users
ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로,
-- 만약 같은 나이라면 계좌 잔고가 많은 순으로 조회
SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

-- 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;

-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users
ORDER BY country DESC;

-- 이름과 지역이 중복없이 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users;

-- 이름과 지역 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;


-- WHERE 실습

-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance FROM users
WHERE age>=30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;



-- LIKE 실습

-- LIKE '김%' => 김으로 시작하는 모든 것 ex. 김밥, 김치냉장고 등
-- LIKE '김_' => 김으로 시작하고 한글자만 더 오는 것 (2글자) ex. 김밥, 김치
-- LIKE '%도' => 도로 끝나는 모든 것 ex. 강원도, 충청북도, 수도
-- LIKE '%강원%' => 강원이 포함되는 모든 것 ex. 강원, 김강원, 강원도, 대한민국 강원도에 살아요
-- LIKE '_도' => 한글자 + 도 ex. 수도, 과도 등
-- LIKE '_2%' => 2자리 이상 ex. 12%, 12534%
-- LIKE '1____' => 무조건 4자리 ex. 1004, 1000, 1111

-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name FROM users
WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '%02-%';

-- 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age LIKE '2_';

SELECT first_name, age FROM users
WHERE age >=20 and age < 30;

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

-- IN
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';

-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강웓도');

SELECT first_name, country FROM users
WHERE country != '경기도' and country != '강원도';

-- BETWEEN
-- 나이가 20살 이상 30살 이하인 사람의 이름, 나이 조회
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;

-- 나이가 20살 이상 30살 이하가 아닌 사람의 이름, 나이 조회
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age < 20 or age > 30;


-- LIMIT
-- 계좌 잔고가 가장 많은 10명 이름, 잔고 조회
SELECT first_name, balance FROM users
ORDER BY balance DESC
LIMIT 10;

-- 나이가 가장 어린 5명의 이름, 나이 조회
SELECT first_name, age FROM users
ORDER BY age ASC
LIMIT 5;


-- OFFSET
-- 11번째부터 20번째 데이터의 rowid와 이름 조회
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;


-- GROUP BY
SELECT country, COUNT(*) FROM users
GROUP BY country;

-- 집계 함수
-- users 테이블의 전체 행 수
SELECT COUNT(*) FROM users;

-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users
WHERE age >= 30;

-- 성 별로 인원 수 출력 (변수명 임시로 변경)
SELECT last_name, COUNT(*) AS number_of_name FROM users
GROUP BY last_name;

-- 많은 성씨 순으로 출력
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;

-- 지역별 평균 나이 조회, 오름차순 정렬
SELECT country, AVG(age) FROM users
GROUP BY country ORDER BY AVG(age) ASC;





-- CREATE
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);


-- INSERT
-- 단일 행 삽입하기
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('임범규', 24, '대전');

-- 여러 행 삽입하기
INSERT INTO classmates
VALUES
('홍길동', 31, '강원'),
('김길동', 27, '서울');



-- UPDATE
-- 데이터 수정
UPDATE classmates
SET name = '김철수한무두루미',
    address = '제주도'
WHERE rowid = 3;


-- DELETE
-- 일부 데이터 삭제
DELETE FROM classmates
WHERE rowid = 7;

-- 모든 데이터 삭제
DELETE FOR classmates

-- 이름에 '홍'이 포함되는 데이터 삭제하기
DELETE FROM classmates
WHERE name LIKE '%홍%';





-- HWS
CREATE TABLE test (
  name TEXT,
  age INT,
  address TEXT
);

INSERT INTO test
VALUES
('홍홍홍', 25, '청주');

-- 생성X
insert into test
values(address = 'seoul', age = 20, name = '홍길동');

-- 생성O
insert into test (address, age, name)
values('seoul', 20, '홍길동');