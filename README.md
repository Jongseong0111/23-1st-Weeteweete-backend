 ## WEETEWEET 프로젝트 Back-end 소개
- "motemote" 커머스 사이트 clone
- 기획이 필요하지 않기 때문에 기본기능 구현에 집중했습니다.
- 개발은 초기 세팅과 데이터 모델링을 직접 진행했으며, 실제 커머스 사이트의 기능을 대부분 구현했습니다.
- 프런트 앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발하였습니다.
- 개발자의 기본 tool인 git과 git hub을 적적하게 사용하였습니다.
- 적절한 역할 분담과 적극적이 의사소통으로 원활하게 프로젝트를 마무리하였습니다.

## 개발 인원 및 기간
- 개발기간 : 2021/8/2 ~ 2021/8/13

- 개발 인원 : 프론트엔드 4명, 백엔드 2명

- 팀원 [프론트엔드]

 - 최호정: nav, footer, 메인페이지, 제품리스트페이지, 상품 리뷰
 - 차예은: 결제 form
 - 배윤아: 로그인/회원가입, 아이디/비밀번호 찾기, 결제 table
 - 이나현: 상세페이지, 장바구니

 [백엔드]

 - 백선호: 로그인/회원가입, 비밀번호 초기화, 아이디 찾기, 로그인 데코레이터, 상품 결제, 상품 리뷰
 - 임종성: 모델링, 메인페이지, 상세페이지, 메뉴페이지, 장바구니 CRUD, 상품 리뷰
 - 
- [프론트엔드 github 링크] : https://github.com/wecode-bootcamp-korea/23-1st-Weeteweete-frontend

## 프로젝트 구현영상
-  https://www.youtube.com/watch?v=_oMzIV2oyxE

# 적용 기술 및 구현 기능

## 적용 기술

- Back-End : Python, Django web framework, Bcrypt, My SQL, RESTful API

## 구현 기능

### 로그인/회원가입
- Bcrypt 암호화, JWT를 이용한 인증/인가
- Fidn Account/UUID Moduel 활용한 Temporary Password 생성 및 저장

### PageView
- Query Paramter와 Ternary Operator 활용하여 Main/Menu 페이지 통합 구현
- 메인 페이지 : 판매량 순 상위 8개 상품 정렬
- 메뉴 페이지 : 상품의 category, option, concept, color 별 분류

### 상품 상세 페이지
- 상품 id를 parameter로 받아 상품 Data와 Review를 표출하는 기능 구현

### 상품 후기
- Django Static 개념 활용하여 Image Fild Upload 기능 구현
- 상품을 구매한 User만 Reveiw 작성 가능하도록 Decorator로 JWT 인가

### 장바구니
- User 장바구니 상품의 C.R.U.D
- Detail Page에서의 Update는 수량 추가, Cart Page에서의 Update는 수량 변경이 되도록 Condition 적용

### 상품 구매
- Item에 대한 OrderStatus, OrderItemStatus를 ENUM(열거형)으로 표현하여 Order Flow 시각화
- Item 구매 시 Item 재고량, 판매수량, Point 변화
- 원자성을 보장하기 위한 Transaction 적용

# Reference

- 이 프로젝트는 모트모트 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
