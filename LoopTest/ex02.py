while True:
    id = input("아이디 입력 (4~12자): ")
    
    if len(id) >= 4 and len(id) <= 12:
        break   
    else:
        print("아이디는 4자 이상 12자 이하여야 합니다. 다시 입력하세요.")

while True:
    pw = input("비밀번호 입력 (8자 이상, 숫자포함): ")
    
    if len(pw) < 8:        
        print("비밀번호는 8자 이상이어야 합니다. 다시 입력하세요.")
        continue
    # 숫자 포함유무 boolean
    digit = False

    # in사용 => for i in 변수
    # 변수 문자열에 들어있는 문자들을 하나씩 꺼내서 i에 넣으며 반복한다
    for ch in pw:
        # 문자가 '0'이상이고 '9'이하면 숫자
        if ch >= '0' and ch <= '9':
            # 숫자가 포함되어 boolean 값변경
            digit = True
            break
    # 숫자가 하나도 없으면 다시 입력
    if not digit:
        print("비밀번호는 숫자가 포함되어야 합니다. 다시 입력하세요.")
        continue
    # 모든조건 만족시 종료하고 다음단계
    break

while True:
    email = input("이메일 입력: ")
    # if @ in 변수 : @가 변수안에 포함되어 있냐는 의미

    if "@" in email:
        break
    print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")                  
        
print("유효성 검사 통과! API 요청을 전송합니다.")    
