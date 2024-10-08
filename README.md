# spartamarket_DRF-

SpartaMarket DRF
이 프로젝트는 Django Rest Framework(DRF)를 사용한 사용자 관리, 프로필 관리, 상품 관리 기능을 제공하는 REST API입니다. 이 프로젝트는 사용자 인증, 프로필 관리, 상품 생성 및 검색 등의 기능을 포함합니다.

주요 기능

1. 사용자 관리

회원가입: 사용자는 회원가입할 수 있으며, 회원가입 시 자동으로 프로필이 생성됩니다.
로그인: 토큰 기반 인증을 통한 안전한 로그인 기능을 제공합니다.
비밀번호 변경: 사용자는 이전 비밀번호와 다른 새 비밀번호를 설정할 수 있도록 유효성 검사를 진행합니다.

2. 프로필 관리

프로필 조회: 사용자는 자신의 프로필을 조회할 수 있습니다.
프로필 수정: 사용자는 프로필 정보를 수정할 수 있으며, 중복된 이메일 또는 사용자 이름을 방지하는 유효성 검사를 포함합니다.  

3. 상품 관리

상품 등록: 로그인한 사용자는 새로운 상품을 등록할 수 있습니다.
상품 목록: 등록된 상품을 페이지네이션 기능을 통해 조회할 수 있습니다.
상품 수정 및 삭제: 사용자는 자신이 등록한 상품을 수정하거나 삭제할 수 있습니다.
상품 검색: 사용자는 제목, 사용자 이름 또는 내용에 기반한 상품 검색 기능을 사용할 수 있습니다.

프로젝트 구조

startamarket_drf/  
├── accounts/          # 사용자 인증(회원가입, 로그인) 및 계정 관련 기능을 관리합니다.  
├── products/          # 상품 생성, 수정, 삭제 및 목록 조회를 담당합니다.  
├── profiles/          # 사용자 프로필 관리를 처리합니다.  
├── startamarket_drf/  # 프로젝트 설정 파일입니다.  
├── db.sqlite3         # SQLite 데이터베이스 파일입니다.  
├── manage.py          # Django 관리 스크립트입니다.  
├── requirements.txt   # 프로젝트의 의존성 파일입니다.  
└── README.md          


설치 방법

1. git clone <repository_url>
2. cd startamarket_drf
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

사용 방법

- 사용자 회원가입

엔드포인트: POST -> /api/accounts/signup/

설명: 사용자는 회원가입 시 이메일, 사용자 이름, 비밀번호 등의 정보를 제출합니다. 제출 후 프로필이 자동으로 생성됩니다.

![회원가입](https://private-user-images.githubusercontent.com/173751168/365873219-00ea8c0a-61a8-4e07-a7bd-ce1cc1ca679e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY0NjksIm5iZiI6MTcyNTkzNjE2OSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMjE5LTAwZWE4YzBhLTYxYTgtNGUwNy1hN2JkLWNlMWNjMWNhNjc5ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQyNDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00N2M1MmNhMzVhNzM0YWJhZTUwZjM2MDhjOTI3MTQxYjEzZjEzZjExNDA1OWZiNGM5Zjk4NTNmYzhhNTJlYTlhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.MCoyRQ-UUi6I3Izr1gjE-XQSOu9UQhtlra8zJuhSvOY)

- 로그인

엔드포인트: POST -> /api/accounts/login/

설명: 사용자는 username와 비밀번호를 사용하여 로그인하고, 토큰 기반 인증을 통해 API에 접근할 수 있는 토큰을 받습니다.

![로그인](https://private-user-images.githubusercontent.com/173751168/365873172-377d39ff-e43b-463e-9418-3b932230aac8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTcyLTM3N2QzOWZmLWU0M2ItNDYzZS05NDE4LTNiOTMyMjMwYWFjOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZDIzZGEzY2Q2OTMzNmM0NWRmMTU0ZTE1NTEyOGM5YjZhNDRhNTE3MjYzNmRhYTZmM2M3Y2Y5ZjY0ZGFmOThmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.-zHrbfrz8nLrccjQ0zjw8nEOx9LEkAqCZDxA8xNbt48)

- 로그아웃

엔드포인트: POST -> api/accounts/logout/

설명: 로그인된 사용자의 토큰 블랙리스트 처리하여 로그아웃합니다.


- 회원 정보 수정

엔드포인트: PUT -> api/accounts/{pk}/

설명: 회원의 username ,email, author, nickname, first_name, PR등을 수정 할 수 있습니다. username과 email은 중복검사를 실시합니다.

![회원 정보 수정](https://private-user-images.githubusercontent.com/173751168/365873215-b7e57428-4a6c-40f3-8984-a45ea818be00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMjE1LWI3ZTU3NDI4LTRhNmMtNDBmMy04OTg0LWE0NWVhODE4YmUwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01YzJhMzAyZTU2ZDdlMzcwMTM5NGJiY2U3MTYxZTUzOGUyOTE3YTE1ODBmZDFjOTAyYmI5N2JiYWY3MDk0OTI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.xbosduTMVky2gAmC_nT5_KGKuzu0bNTSgM4c2TROdkM)

- 비밀번호 변경

엔드포인트: PUT -> /api/accounts/password/change/

설명: 기존 비밀번호와 새비밀번호를 각각 검증하여 비밀번호 변경을 진행. 단, 기존 비밀번호가 일치하지 않거나, 새 비밀번호가 보안에 취약하다면 다시 입력 받습니다.
![비밀번호 변경(성공)](https://private-user-images.githubusercontent.com/173751168/365873176-12e350d0-97dc-46bd-bf86-64ea33e53c78.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTc2LTEyZTM1MGQwLTk3ZGMtNDZiZC1iZjg2LTY0ZWEzM2U1M2M3OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mYmYyZTM5NmUyYzY4MjJlMmQwYWFkMTM2YmU4YzU1NjBiYjNiMGVlNWI3OTM5MzM4YjZhYWE4MDk4YzRhNzkxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.XS3mMFGtMYC0r1crO7SXmkjyAK8IaHMtbqB2XGndsD0)
![비밀번호 변경(실패)](https://private-user-images.githubusercontent.com/173751168/365873180-31008a90-995d-496e-adc1-99b9dbcf3fd3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTgwLTMxMDA4YTkwLTk5NWQtNDk2ZS1hZGMxLTk5YjlkYmNmM2ZkMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZGNiODg5OGViYWQ2MDJiN2JhYmE0MzIzYmQ1MTUzOTdlMzk4NzNkNjIyMmI3OTVlMGE3YWI0MTA3NjgzMTY3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.I8KNaCmFTgCy8zpPDk_xsyeM19LN9DlirOykc5Ir8Pc)
![비밀번호 변경(실패)](https://private-user-images.githubusercontent.com/173751168/365873186-1b25a038-6bde-4618-865e-43f90e74e3d3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTg2LTFiMjVhMDM4LTZiZGUtNDYxOC04NjVlLTQzZjkwZTc0ZTNkMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zM2IwNzgwMzcxOGJmYWJmMDVhNjQ5ZTg0NGJkNWE1ZDhiODZkODliYzY2YWVhNmFiM2RiMzUyOGFkOWNlOGI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.C0j9VV2CVRW9WpJUSje5h5B49PwpXsKefhMVLkXq9kQ)

- 프로필 조회

엔드포인트: GET -> /api/profiles/{username}/

설명: 사용자는 자신 또는 다른 사용자의 프로필 정보를 조회할 수 있습니다.

![프로필 조회](https://private-user-images.githubusercontent.com/173751168/365873207-f79fd72a-336b-4f83-a47c-d5521bdb3e33.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMjA3LWY3OWZkNzJhLTMzNmItNGY4My1hNDdjLWQ1NTIxYmRiM2UzMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jNTJlNWVlZTBhODgxMDg2MDk3YmNjNDBkNmNiYWExNjU1YzBhYjM0NjcwOWNiNWQwYTNlMDc3M2VjMGUzZjI4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.V8-oOyNwMWoxY752EQkqHETmc1TlTjlAu4Dk8SrqEU4)

- 프로필 수정

엔드포인트: PUT -> /api/profiles/{username}/

설명: 사용자는 자신의 프로필 정보를 수정할 수 있습니다.

![프로필 수정](https://private-user-images.githubusercontent.com/173751168/365873204-d7b55e56-294d-41a8-bcbe-840f46bb26bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMjA0LWQ3YjU1ZTU2LTI5NGQtNDFhOC1iY2JlLTg0MGY0NmJiMjZiZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xOTc5MzNhYTU0MDUyOTIzNmQ5NmFiYTc1NGYwMDhkYTA3ZDY3Yzc5N2IwZjNjOTJlOTIwMjMxM2RiNWUyMjhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.7-TJhPbGXTXCRdFWy0ZE6zYe3hHIBH2zbxmu3bi-jQw)

- 상품 등록

엔드포인트: POST -> /api/products/

설명: 사용자는 로그인을 통해 인증된 상태에서 새로운 상품을 등록할 수 있습니다.

![상품 등록](https://private-user-images.githubusercontent.com/173751168/365873191-f4c92a75-a891-49d7-9e9a-52993dcca1b0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTkxLWY0YzkyYTc1LWE4OTEtNDlkNy05ZTlhLTUyOTkzZGNjYTFiMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MTE0ZjA5MzM2ZDVhOWIwZjE0YjI1OTM5YzFkZTQwZDE1YjFhOWY5MmVlYThiODBmZmQ5NzgzOTcxZjcwMDYwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.hyDam015KJ_KbbEtTpN9D9YjaT3G_ppaBZuRdAZERxs)


- 상품 조회

엔드포인트: GET -> /api/products/{pk}/

설명: 등록한 상품의 상세페이지를 볼 수 있습니다.

![상품조회](https://private-user-images.githubusercontent.com/173751168/365873166-985faa83-2975-4566-ac78-71da1b53e054.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTY2LTk4NWZhYTgzLTI5NzUtNDU2Ni1hYzc4LTcxZGExYjUzZTA1NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZjg2MTIzNDkxMWY3ZjU4YWNlZWE1NjVjNjRmYTA3ZjhiNjE5YTMzNWVhMzI4ZTIxNjk3ZTA4ZDJiODU0NzczJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.SIpRNMuXMViDF0cvRjOPeKgWrVF8fTpDtPdFbUEMz7A)



- 상품 목록

엔드포인트: GET -> /api/products/

설명: 등록된 상품의 목록을 페이지네이션 기능과 함께 조회할 수 있습니다.

![상품 목록](https://private-user-images.githubusercontent.com/173751168/365873196-85952624-2b99-4fb4-995a-aeb2143f3708.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTk2LTg1OTUyNjI0LTJiOTktNGZiNC05OTVhLWFlYjIxNDNmMzcwOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYTk3NDQzYjA3YmJjMjFiYjQwMDM0ZDI2NjcxMzQzYTBiODhmMDRlNjdjYjI2MTc0MDBiNTE0OTIzZDc3ZWNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.z4plTc5f5_hliuo3EAr0ZLT9Zpr01V76zcbxVpP1ONI)

- 상품 수정

엔드포인트: PUT -> /api/products/{id}/

설명: 사용자는 자신이 등록한 상품 정보를 수정할 수 있습니다.

![상품 수정](https://private-user-images.githubusercontent.com/173751168/365873164-54943ee4-6d3c-4ab7-bcf3-5ea805ed759e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTY0LTU0OTQzZWU0LTZkM2MtNGFiNy1iY2YzLTVlYTgwNWVkNzU5ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNDcyNjFmZTc1NTM3ODNkODIzOWNiNjlmZWY2N2M4NWVkYTI5ODg3NzY2MzUzOWQ0ODFiZmMyNjRkYjRmYTE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.5sl5rSA6D8Z7SzxUrUjdau5uYtyIZVwUGhMStVrvhKg)

- 상품 삭제

엔드포인트: DELETE -> /api/products/{id}/

설명: 사용자는 자신이 등록한 상품을 삭제할 수 있습니다.

![상품 삭제](https://private-user-images.githubusercontent.com/173751168/365873188-a26adf1c-a56f-4bda-8911-785e958d3420.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTg4LWEyNmFkZjFjLWE1NmYtNGJkYS04OTExLTc4NWU5NThkMzQyMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iNjRlZmJjMGYwMjYxYjljODBlODYxNmQ1ODRhNGFlOTM0YWQzODYwNmYwMGZiNmQ2YjRlYjZkNDUyZGMwYzE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.NvKGBBJyCm5NOc4QgeQ81KzvaGz05V5dv2ohOFSF8TA)

- 상품 검색

엔드포인트: GET -> /api/products/search/?q=<query>

설명: 사용자는 상품 제목, 사용자 이름 또는 상품 설명을 기준으로 상품을 검색할 수 있습니다.

![상품 검색](https://private-user-images.githubusercontent.com/173751168/365873161-833eba7e-8e6a-4fd4-871e-7845a1659dc7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5MzY2NjUsIm5iZiI6MTcyNTkzNjM2NSwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTYxLTgzM2ViYTdlLThlNmEtNGZkNC04NzFlLTc4NDVhMTY1OWRjNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMjQ2MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZmM5YzM3ZmE4MWJkZDk5OGM0MzUzZWNhNjE3MDYyN2E4Nzk4NzJiMmU3ZmZmNmRjN2Y2NmJlYTViY2MxNTVjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.i-23cZ4B65ZAmQC6wvaCYqdR3azZXTthcPrgPysU9uY)



- 카테고리 생성

엔드포인트: POST -> api/products/category/

설명: admin은 새로운 카테고리를 등록할 수 있습니다. admin 권한이 없는 사용자는 카테고리를 생성할 수 없습니다

![카테고리 생성(admin)](https://private-user-images.githubusercontent.com/173751168/365873157-d4196d4c-d8a7-4939-83ef-5278b90979cf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5NDE2MzQsIm5iZiI6MTcyNTk0MTMzNCwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMTU3LWQ0MTk2ZDRjLWQ4YTctNDkzOS04M2VmLTUyNzhiOTA5NzljZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwNDA4NTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YjU4ZjFiZTZhNjMzNjljNjZkODIxYjY5ZTFkNDU2M2JiZmQ3ODE0MjljMzhlMTQzODY2YzlkMTQyMjhiODBmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.c2vt65mh8fSZ62zRlu6muN36tGWs45gM34Jsep6xfuA)

![카테고리 생성불가(user)](https://private-user-images.githubusercontent.com/173751168/365873201-60b94298-8ec4-4feb-9ff7-ef62f30db3b6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5NDE2MzQsIm5iZiI6MTcyNTk0MTMzNCwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODczMjAxLTYwYjk0Mjk4LThlYzQtNGZlYi05ZmY3LWVmNjJmMzBkYjNiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwNDA4NTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMmYyYTg5ZjUyNTFhMjkyN2MyNDQwNjY2ZDJlZjE1ZTFhNGRkNDkyNDM5N2YwNTJhYzIxNmVkYmUyZTlkMjkzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.3aSfstluu4lo0C9Pi0xmW8etVjyO6BFRoE8gxTM9nwI)

사용 기술

Django
Django Rest Framework
SQLite
토큰 기반 인증 (JWT)
Python


ERD

![ERD](https://private-user-images.githubusercontent.com/173751168/365884256-00614fac-ebe0-4f58-a713-a825d242ad8f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5Mzk5NjQsIm5iZiI6MTcyNTkzOTY2NCwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODg0MjU2LTAwNjE0ZmFjLWViZTAtNGY1OC1hNzEzLWE4MjVkMjQyYWQ4Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMzQxMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjFjZDI0YWY0NjE1N2UyYmYyNzc5ZTU3MDQzNzc0Mzg4OGU1MmYyMWE1MDVkYmFkY2M0NWFhZGQ2ZGIzMTE2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.M9M-3QRAEwJXeZrb9F_r9hwbFkmEQSOYIgBnaWpRUNo)

# SpartaMarket DRF

This project provides a REST API for user management, profile management, and product management using Django Rest Framework (DRF). The project includes features such as user authentication, profile management, product creation, and search functionalities.

## Key Features

### 1. User Management
- **Signup**: Users can sign up, and a profile is automatically created upon registration.
- **Login**: Secure login with token-based authentication.
- **Password Change**: Users can change their password with validation to ensure it differs from the old one.

### 2. Profile Management
- **View Profile**: Users can view their profile.
- **Edit Profile**: Users can update profile information with validation to prevent duplicate emails or usernames.

### 3. Product Management
- **Create Product**: Logged-in users can create new products.
- **View Products**: Products can be viewed with pagination.
- **Edit and Delete Product**: Users can edit or delete products they have created.
- **Search Product**: Users can search products by title, username, or content.

## Project Structure

```text
spartamarket_drf/
├── accounts/          # Manages user authentication and account-related functionality (signup, login).
├── products/          # Handles product creation, update, deletion, and listing.
├── profiles/          # Manages user profile data.
├── spartamarket_drf/  # Project settings.
├── db.sqlite3         # SQLite database file.
├── manage.py          # Django management script.
├── requirements.txt   # Project dependencies.
└── README.md

## Installation
1. Clone the repository: `git clone <repository_url>`
2. Navigate into the project directory: `cd spartamarket_drf`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## Usage

### User Signup
- **Endpoint**: `POST /api/accounts/signup/`
- Users can sign up by providing an email, username, and password. A profile is automatically created upon signup.

### Login
- **Endpoint**: `POST /api/accounts/login/`
- Users can log in using their username and password, and receive a token for authenticated API access.

### Logout
- **Endpoint**: `POST /api/accounts/logout/`
- Logged-in users can log out, and their token will be blacklisted.

### Update User Information
- **Endpoint**: `PUT /api/accounts/{pk}/`
- Users can update their information such as username, email, and profile details. Username and email are validated to avoid duplicates.

### Change Password
- **Endpoint**: `PUT /api/accounts/password/change/`
- Users can change their password by providing the old password and a new password.

### View Profile
- **Endpoint**: `GET /api/profiles/{username}/`
- Users can view their own or other users' profile information.

### Edit Profile
- **Endpoint**: `PUT /api/profiles/{username}/`
- Users can update their own profile information.

### Create Product
- **Endpoint**: `POST /api/products/`
- Logged-in users can create new products.

### View Product
- **Endpoint**: `GET /api/products/{pk}/`
- Users can view the details of a specific product.

### View Product List
- **Endpoint**: `GET /api/products/`
- Users can view a paginated list of products.

### Edit Product
- **Endpoint**: `PUT /api/products/{id}/`
- Users can update products they have created.

### Delete Product
- **Endpoint**: `DELETE /api/products/{id}/`
- Users can delete products they have created.

### Search Products
- **Endpoint**: `GET /api/products/search/?q=<query>`
- Users can search for products by title, username, or description.

### Create Category (Admin only)
- **Endpoint**: `POST /api/products/category/`
- Admin users can create new product categories.

## Technologies Used
- Django
- Django Rest Framework
- SQLite
- JWT-based authentication
- Python

## ERD
![ERD](https://private-user-images.githubusercontent.com/173751168/365884256-00614fac-ebe0-4f58-a713-a825d242ad8f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU5Mzk5NjQsIm5iZiI6MTcyNTkzOTY2NCwicGF0aCI6Ii8xNzM3NTExNjgvMzY1ODg0MjU2LTAwNjE0ZmFjLWViZTAtNGY1OC1hNzEzLWE4MjVkMjQyYWQ4Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxMFQwMzQxMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjFjZDI0YWY0NjE1N2UyYmYyNzc5ZTU3MDQzNzc0Mzg4OGU1MmYyMWE1MDVkYmFkY2M0NWFhZGQ2ZGIzMTE2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.M9M-3QRAEwJXeZrb9F_r9hwbFkmEQSOYIgBnaWpRUNo)
