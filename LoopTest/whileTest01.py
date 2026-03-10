# while 조건:
# 실행 구문
# 파이썬은 break, continue 사용가능
# 단, return은 함수에서만 사용가능
response = "아니"
while response == "아니":
    response = input("엄마, 다 됐어?")

print("먹자")


# break 이용해서 수정
# 파이썬에서 boolean값은 반드시 True,False
# 첫 글자를 대문자로 입력
 
while True:
    response2 = input("엄마, 다 됐어?")
    if response2 != "아니":
        break
    
print("먹자")
