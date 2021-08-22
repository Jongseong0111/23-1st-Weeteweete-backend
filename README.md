 # WeeteWeete(위트위트)
 
 ## Introduction To WeeteWeete Project

 > Colorize your life with weete weete<br/>
 > 색은 특별함을 담는 가장 강력한 요소입니다. <br/>
 > 'color'라는 가치관에 생각과 감정을 정리하는 노트를 판매하는 모트모트 페이지가 매력적으로 느껴졌습니다. <br/>
 > 모트모트만의 매력과 페이지의 디자인/기획이 마음에 들어 디자인/기획 부분만 클론했습니다. <br/>
 > 개발은 초기 세팅부터 직접 구현했으며, 데모 영상에서 알 수 있듯이 모든 부분이 백앤드와 통신으로 이루어져 있습니다. 

## WeeteWeete Team & Term
- 개발기간 : 2021/8/2 ~ 2021/8/13

- 개발 인원 : 프론트엔드 4명, 백엔드 2명

- 팀원 [프론트엔드]
 - [프론트엔드] : 최호정, 차예은, 배윤아, 이나현
 - [백엔드] : 백선호, 임종성

- [프론트엔드 github 링크] : https://github.com/wecode-bootcamp-korea/23-1st-Weeteweete-frontend

## Project Video
-  https://www.youtube.com/watch?v=_oMzIV2oyxE

## 적용 기술 및 구현 기능

### 적용 기술

- Back-End : Python, Django web framework, Bcrypt, My SQL, RESTful API

### 구현 기능

#### SignIn/SignUp
- Bcrypt 암호화, JWT를 이용한 인증/인가
- Fidn Account/UUID Moduel 활용한 Temporary Password 생성 및 저장

#### PageView
- Query Paramter와 Ternary Operator 활용하여 Main/Menu 페이지 통합 구현
- 메인 페이지 : 판매량 순 상위 8개 상품 정렬
- 메뉴 페이지 : 상품의 category, option, concept, color 별 분류

#### DetailPage
- 상품 id를 parameter로 받아 상품 Data와 Review를 표출하는 기능 구현

#### Review
- Django Static 개념 활용하여 Image Fild Upload 기능 구현
- 상품을 구매한 User만 Reveiw 작성 가능하도록 Decorator로 JWT 인가

#### Cart
- User 장바구니 상품의 C.R.U.D
- Detail Page에서의 Update는 수량 추가, Cart Page에서의 Update는 수량 변경이 되도록 Condition 적용

#### Purchase
- Item에 대한 OrderStatus, OrderItemStatus를 ENUM(열거형)으로 표현하여 Order Flow 시각화
- Item 구매 시 Item 재고량, 판매수량, Point 변화
- 원자성을 보장하기 위한 Transaction 적용

## Reference

- 이 프로젝트는 모트모트 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

- 모트모트: https://motemote.kr/
