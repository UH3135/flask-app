# flask-app

file structure
/your_flask_app
│── app/
│   ├── _init__.py        # Flask 앱 및 확장 초기화
│   ├── config.py          # 각 환경별 설정
│   ├── routes.py          # 블루프린트 없이 공통 라우트 관리 (필요 시)
│   ├── extensions.py      # Flask 확장 (DB, Migrate 등) 초기화
│   ├── models.py          # 데이터베이스 모델 정의
│   ├── blueprints/
│   │   ├── _init__.py    # 블루프린트 등록
│   │   ├── auth/          # 인증 관련 블루프린트
│   │   │   ├── _init__.py 
│   │   │   ├── routes.py  # 로그인, 회원가입 등 API
│   │   │   ├── models.py  # Auth 관련 모델 (User 등)
│   │   │   ├── forms.py   # Flask-WTF 폼 (선택 사항)
│   │   ├── main/          # 메인 블루프린트 (홈, 대시보드 등)
│   │   │   ├── _init__.py 
│   │   │   ├── routes.py
│   │   │   ├── templates/
│   │   │   ├── static/
│── instance/
│   ├── config.py          # 비밀 키 및 환경 변수
│── migrations/            # Flask-Migrate 마이그레이션 폴더
│── run.py                 # 앱 실행 파일
│── requirements.txt
│── .env                   # 환경 변수
│── .gitignore