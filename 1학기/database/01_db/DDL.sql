-- create
-- 데이터 테이블 생성
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);


-- alter table
-- 데이터 테이블 이름 수정
ALTER TABLE contacts
RENAME TO new_contacts;

-- 데이터 테이블 구조 수정
ALTER TABLE new_contacts
RENAME COLUMN name TO last_name;

-- 데이터 테이블에 새로운 column 추가
ALTER TABLE new_contacts
ADD COLUMN address TEXT NOT NULL;

-- 데이터 테이블에서 column 삭제
ALTER TABLE new_contacts
DROP COLUMN address;


-- drop table
-- 테이블 삭제
DROP TABLE new_contacts

