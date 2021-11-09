# Asignment3
원티드x위코드 백엔드 프리온보딩 과제3
- 과제 출제 기업 정보
  - 기업명 : 원티드랩
  
## Members
|이름   |Github                   |Blog|
|-------|-------------------------|--------------------|
|이태성 |[yotae07](https://github.com/yotae07)     | 추가   |
|임유선 |[YusunL](https://github.com/YusunL)   | 추가   |
|윤현묵 |[fall031-muk](https://github.com/fall031-muk) | https://velog.io/@fall031   |
|김정수 |[hollibleling](https://github.com/hollibleling) | https://velog.io/@hollibleling  |
|최현수 |[filola](https://github.com/filola) | https://velog.io/@chs_0303 |

## 과제 내용
- 원티드 선호 기술스택: Python flask 또는 fastapi
> 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요.

</aside>

### [필수 포함 사항]
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### [개발 요구사항]

✔️ **데이터**
---

- 회사 정보
    - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
    - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
  
- 데이터셋 예제
    - 원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)

✔️ **REST API 기능**
---

- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

✔️ **개발 조건**
---
- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.

## 구현 기능
### 로그인 기능
- 내용추가

### 상품 관리 기능
- 상품 전체목록 조회 가능 및 페이징 기능(한 페이지당 5개 상품)
- 사용자는 상품 조회만 가능하며 관리자는 상품 추가/수정/삭제 가능

## API

## 실행 방법(endpoint 호출방법)

### ENDPOINT

| Method | endpoint | Request Header | Request Body | Remark |
|:------:|-------------|-----|------|--------|
|POST|/user||email, password, role|회원가입|
|POST|/api/token/||email, password|로그인|
|POST|/product|bearer token|category, name, description, isSold, badge|상품 등록|
|GET|/product|bearer token|    |전체 상품 조회|
|GET|/product/product_id|bearer token|    |개별 상품 조회|
|PATCH|/product/product_id|bearer token|category, name, description, isSold, badge|상품 수정|
|DELETE|/product/product_id|bearer token|| 상품 삭제 |
|POST|/product/product_id/item|bearer token|name, size, price, isSold, menuid|상품 아이템 등록|
|PATCH|/product/product_id/item/item_id|bearer token|name, size, price, isSold, menuid|상품 아이템 수정|
|DELETE|/product/product_id/item/item_id|bearer token||상품 아이템 삭제|
|POST|/product/product_id/tag|bearer token|name, type, menuid|상품 태그 등록|
|PATCH|/product/product_id/tag/tag_id|bearer token|name, type, menuid|상품 태그 수정|
|DELETE|/product/product_id/tag/tag_id|bearer token||상품 태그 삭제|


## API 명세(request/response)

[post man 링크](https://documenter.getpostman.com/view/17228945/UVC3j7ZC#intro)


## 폴더 구조
```
├── company
│   ├── __init__.py
│   ├── migrations           
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── pytest.ini
├── requirements.txt
├── README.md
├── test_app.py
└── wanted
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
