# 비밀번호 입력
pw = input("비밀번호 입력 : ")

# 8자이상 체크
check1 = 0
# 대문자체크
check2 = 0
# 소문자체크
check3 = 0
# 숫자체크
check4 = 0
# 특수문자체크
check5 = 0

# 8자 이상체크
if len(pw) >= 8:
    print("[√]",end="")
    # 강도누적
    check1 = 1
else:        
    print("[X]",end="")
print(" 길이 8자 이상")

# for문 돌려서 체크
for ch in pw:   
    # 대문자 누적
    if ch >= 'A' and ch <= 'Z':
        check2 = 1
    # 소문자 누적
    elif ch >= 'a' and ch <= 'z':
        check3 = 1
    # 숫자 누적
    elif ch >= '0' and ch <= '9':
        check4 = 1
    # 특수문자 누적
    else:
        check5 = 1

# 대문자
if check2 > 0:
    print("[√]",end="")
else:
    print("[X]",end="")
print(" 대문자 포함")

# 소문자
if check3 > 0:
    print("[√]",end="")
else:
    print("[X]",end="")
print(" 소문자 포함")

# 숫자
if check4 > 0:
    print("[√]",end="")
else:
    print("[X]",end="")
print(" 숫자 포함")

# 특수문자
if check5 > 0:
    print("[√]",end="")
else:
    print("[X]",end="")
print(" 특수문자 포함")

# 강도합계
strength = check1 + check2 + check3 + check4 + check5

print("비밀번호 강도: ",end="")
if strength >= 5:
    print(" 매우 강함")
elif strength < 5 and strength >= 4:
    print(" 강함")
elif strength < 4 and strength >= 3:
    print(" 보통")
elif strength < 3 and strength >= 2:
    print(" 약함")
else:
    print(" 매우 약함")