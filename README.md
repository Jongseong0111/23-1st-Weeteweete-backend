 ## 📓 WeeteWeete 프로젝트 소개
 
 ![image](https://user-images.githubusercontent.com/84963683/136541442-e10a989e-e8e1-4a7d-a41a-98091e12cb19.png)

 **Color라는 가치관을 담아내 감각적이고 심플하지만 강력한 구성, 부드러운 필기감을 구현한 [모트모트](https://motemote.kr/contents/collabs.html) Motive Project**
 
 > Colorize your life with weete weete<br/>
 > 색은 특별함을 담는 가장 강력한 요소입니다. <br/>
 > 2주라는 짧은 프로젝트 기간 내에 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.   
 > 개발은 초기 세팅과 데이터 모델링을 직접 진행하고 실제 MoteMote 사이트의 기능을 대부분 구현했습니다.   
 > 시연영상에 나오는 부분은 Frontend - Backend간 통신으로 실제 사용할 수 있는 서비스 수준으로 개발했습니다.   

## 개발 인원 및 기간
- [총 프로젝트 기간] : 2021.08.02 ~2021.08.13
- [개발 인원] 
  - Frontend 4명(최호정, 차예은, 배윤아, 이나현)
  - Backend 2명(백선호, 임종성)

## Database Modeling
![image](https://user-images.githubusercontent.com/84963683/136546044-936b7119-9def-4104-9780-ab4b9efcc540.png)

## 프로젝트 구현 페이지

[시연영상](https://www.youtube.com/watch?v=_oMzIV2oyxE)

### 메인

![main](https://user-images.githubusercontent.com/84963683/136560747-69a0c5e0-2c32-4f8b-92d6-f6d3fc3a3e42.gif)

### 로그인 / 회원가입
![로그인](https://user-images.githubusercontent.com/84963683/136559571-437f4173-1fae-43c6-82ec-c29f5ae3a2c1.gif)

![회원가입](https://user-images.githubusercontent.com/84963683/136559591-405ff159-a59b-4c55-9453-97de43cb659c.gif)

### 장바구니 / 주문
![장바구니](https://user-images.githubusercontent.com/84963683/136560776-29515133-7a50-4d1a-826a-2c6a7842c984.gif)

![주문](https://user-images.githubusercontent.com/84963683/136560791-e412e736-1f6d-42f3-9ee4-4655e36da701.gif)

![주문2](https://user-images.githubusercontent.com/84963683/136560800-e75b5e32-e416-4296-b144-8f8651d956c3.gif)

## 사용 기술

[Backend] : Python, Django
[DevOps] : Mysql, AWS EC2, RDS, POSTMAN

## 구현 기능

내가 구현한 기능🙌

### Members🙌

- Bcrypt 암호화와 JWT를 이용한 로그인 / 회원가입
- 사용자의 편의를 위한 아이디 찾기 
- UUID 모듈을 활용한 임시비밀번호 생성 

### Products🙌

- Main/Menu Page를 하나의 API로 통합
- Query parameter를 활용해 상품 필터링(Category, Option, Concept, Color 등) 
- Django Static Module을 사용해 상품 리뷰 이미지 파일을 Local에 저장
- 상품 상세 정보 확인 API 구현
- 평점과 작성시간을 기준으로 상품 후기를 정렬
- 상품을 구매한 사용자만 후기 작성이 가능하도록 Login Decorator 활용

### Orders🙌

- 상품 장바구니의 C.R.U.D API
- Orderstatus를 ENUM으로 표현하여 Order Flow 시각화
- 상품 구매 API에 Transaction을 적용해 원자성을 보장
- 상품 구매시 재고량 / 포인트 / 판매수량 / 상태 변화 구현

## 커뮤니케이션

### Stand Up Meeting

매일 11시 Stand Up Meeting을 통해 In progress - Done과 Front-Back간 소통을 진행하고 매주 Sprint Meeting을 실행했습니다.

### Trello

![image](https://user-images.githubusercontent.com/84963683/136553563-1a702ad0-24ed-48f4-bc76-3dbe213a7055.png)

Front/Back으로 라벨을 분류하고 담당자를 표기하여 직관적으로 확인할 수 있도록 했습니다.

### [Google Spreadsheet(API Documentation)](https://docs.google.com/spreadsheets/d/1PQloL3tWtjEiXV1-C4fMiV3jH8Ei1RrNkqakNAejlLo/edit?usp=sharing)

![image](https://user-images.githubusercontent.com/84963683/136554959-d7457e76-e529-48e6-aaef-8dbafd8f420d.png)

API별 기능, URL, Request 및 Response Key Value와 특이사항을 정리하여 프론트엔드와 공유하였습니다.

## Reference

- 이 프로젝트는 모트모트 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
