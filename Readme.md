1. 2022년 8월 26일

1.1 진행 상황
  - Local PostgreSQL-Firebase 사용 code 완료
  - Cloud SQL-Firebase 사용 code 완료

1.2 주요 사항
  - **Dockerfile 내의 USE_LOCAL_POSTGRESQL를 true로 정의하면 Local DB를 사용함**
  - cloud_sql_proxy 명령을 Docker 내에 넣음
  - 전체 코드 흐름: https://londonappdeveloper.com/deploying-django-to-google-app-engine-using-docker/
  - Running Django on the App Engine standard environment (https://cloud.google.com/python/django/appengine#create-backing-services): Google Cloud Project 생성, 서비스 계정 생성, 권한 부여, 비밀관리자(Secret Manager) 사용 및 .env 파일 생성
  - Django 및 PostreSQL 관련 내용: https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
  - Firebase관련 인증: Firebase Admin SDK 추가 (https://firebase.google.com/docs/admin/setup?hl=ko#python)
  - API 사용설정: Secret Manager API, 
![](../../../../../../../var/folders/0w/12x04bvj38z8v587jfkxm32m0000gn/T/TemporaryItems/NSIRD_screencaptureui_JIbjA0/스크린샷 2022-09-27 오후 2.07.01.png)


  - 보안 키 생성 및 다운로드: **IAM 및 관리자 -> 서비스계정 -> 이메일선택 -> 키 생성**의 순서로 진행함. 이 키를 가지면 Google cloud, firebase 모두 인증 가능
  - 명령
    - Google Cloud 사용자 인증: gcloud auth application-default login
    - gcloud config set project PROJECT_ID
    - psql -h 127.0.0.1 -U kakaocalldb_user0000 -d kakaocalldb00
    - cloud_sql_proxy -instances="djangogaeproject:asia-northeast3:kakaocallpostgresqlinstance"=tcp:5432
    - CREATE TABLE demo_person (id SERIAL PRIMARY KEY, first VARCHAR(32) NOT NULL, last VARCHAR(32) NOT NULL, born VARCHAR(32) NOT NULL);
    - ALTER TABLE demo_person OWNER TO kakaocalldb_user0000;
    - ALTER TABLE demo_person OWNER TO postgres;
    - INSERT INTO demo_person VALUES (5, 'test1', 'test2', 'test3');
    - SELECT * FROM demo_person;
    - DELETE FROM demo_person WHERE id = 5;
    - docker-compose run app python manage.py migrate demo
    - docker-compose run app python manage.py makemigrations demo
    - docker-compose run app python manage.py migrate
    - docker-compose run app python manage.py makemigrations
    - docker-compose run app python manage.py createsuperuser

- 스크린 샷 (기록을 위하여 남김)
    - 서비스 계정
  ![](ScreenShots/ServiceAccount.png)

2. 2022년 9월 30일
2.1 진행 상황
   - 프로젝트: kakaocall-0929
   - Compute Engine 상에서 Web 페이지와 firebase연동을 확인 (Django admin도 확인)

2.2 주요 내용
  - AWS와 Compute Engine에서 모두 동작 확인 
  - AWS: 3.36.135.87
  - Compute Engine: 34.64.231.137
  - Compute Engine 및 AWS에서 sudo make local로 웹페이지 구동 가능
  - PostgreSQL을 Docker에 이미지로 삽이된 것을 사용 
  - Compute Engine을 사용하기 때문에 Deploy 과정이 필요 없음
  - yml 파일의 version을 3.3으로 변경하여야 함
  - firebase의 데이터가 변경된 경우에 웹페이지에 즉시 반영되지 않는 부분 수정 필요

3. 2022년 10월 1일
3.1 진행 상황
   - 프로젝트 directory: kakaocall-1001 (project ID=kakaocall-0929로 유지) 
   - 새로운 Repo 생성: semifive-rvv 관련 문제