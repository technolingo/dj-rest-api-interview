Coding Interview Task - Django REST API
==========

**GET STARTED:**

``docker-compose -f local.yml build``
``docker-compose -f local.yml up``

**MANAGEMENT COMMANDS:**

``docker-compose -f local.yml run --rm django python manage.py migrate``
``docker-compose -f local.yml run --rm django python manage.py createsuperuser``

**FEATURES:**

- 12-Factor setup.
- Docker
- Python/Django
- Django-REST-Framework
- Django ORM, PostgreSQL
- Permissions

-----

TASK DESCRIPTION:

아래 Specification을 만족하는 API 서버를 작성해주세요.

00. Technical Stack:
``Docker``, ``Python``, ``Django``, ``Django REST Framework``, ``Django ORM``, ``PostgreSQL`` 을 사용해주세요.

01. API Specification:
공통
- 커스텀 권한을 추가할 수 있어야합니다.
- 권한은 권한명(str, max_length=16)을 필수로 가집니다.
- 권한은 자식 권한을 가질 수 있으며 부모 권한을 가진 사람은 자식 권한을 모두 가진 것으로 간주합니다. (권한은 최대 2 Level 까지만 가능합니다. 자식 권한의 자식 권한은 존재하지 않습니다. 단, 자식 권한이 존재하지 않을 수도 있습니다.)
- 토큰은 무작위로 생성하되, 중복될 수 없습니다.
- 실패 시 적절한 HTTP 상태코드와 사유를 message로 응답하여야합니다.

토큰 발급 API
Request Body::

    POST /token HTTP/1.1
    Content-Type: application/json

    {"email": "hello@handys.co.kr", "password": "hello_password?"}
    Response Body (Success)

    HTTP/1.1 200 OK
    Content-Type: application/json

    {"success": true, "message": "성공", "token": "token"}
    권한 확인
    Request Body

    GET /permission/{permission_name} HTTP/1.1
    Response Body (Success)

    HTTP/1.1 200 OK
    Content-Type: application/json

    {"success": true, "message": "성공"}
