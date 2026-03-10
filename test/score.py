name = input("이름을 입력하세요")
language = int(input("국어 점수를 입력하세요"))
english = int(input("영어 점수를 입력하세요"))
math = int(input("수학 점수를 입력하세요"))

# 총점
total = language + english + math
# 평균
avg = total/3

print("-" * 80)

print(f"이름 : {name}점")
print(f"국어 : {language}점")
print(f"영어 : {english}점")
print(f"수학 : {math}점")

print("-" * 80)

if language < 40 or english < 40 or math < 40:
    print("과락 - 무조건 F")
else:
    print(f"총점 : {total}점")
    print(f"평균 : {avg:.2f}점")
    if avg>=90:
        print(f"학점 : A")
    elif avg<90 and avg>=80:
        print(f"학점 : B")
    elif avg<80 and avg>=70:
        print(f"학점 : C")
    elif avg<70 and avg>=60:
        print(f"학점 : D")
    else:
        print(f"학점 : F")
