status = int(input("상태코드를 입력하세요"))
# 상태코드
if status == 200:
    print("상태: 200 OK - 요청 성공")
elif status == 201:
    print("상태: 201 Created - 리소스 생성 성공")
elif status == 400:
    print("상태: 400 Bad Request - 잘못된 요청")
elif status == 401:
    print("상태: 401 Unauthorized - 인증 필요")
elif status == 403:
    print("상태: 403 Forbidden - 접근 권한 없음")
elif status == 404:
    print("상태: 404 Not Found - 리소스 없음")
elif status == 500:
    print("상태: 500 Internal Server Error - 서버 내부 오류")
else:
    print(f"상태: {status} Unknown Status Code")

# 계열은 따로
if status >= 200 and status <= 299:
    print("계열: 2xx - 성공")
elif status >= 400 and status <= 499:
    print("계열: 4xx - 클라이언트 오류")
elif status >= 500 and status <= 599:
    print("계열: 5xx - 서버 오류")
