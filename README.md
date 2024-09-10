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
└── README.md          # 본 파일입니다.

설치 방법

1. git clone <repository_url>
2. cd startamarket_drf
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

사용 방법

사용자 회원가입
엔드포인트: POST /api/accounts/signup/

설명: 사용자는 회원가입 시 이메일, 사용자 이름, 비밀번호 등의 정보를 제출합니다. 제출 후 프로필이 자동으로 생성됩니다.

![게시글 검색](./images/게시글%20검색.png)