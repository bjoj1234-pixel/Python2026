score = int(input("점수를 입력하세요: "))

def get_grade(sc):
    grade = ""

    if sc >= 90:
        grade = "A"
    elif sc >= 80:
        grade = "B"
    elif sc >= 70:
        grade = "C"
    else:
        grade = "F"

    print(f"학생의 학점은 {grade}입니다.")    


get_grade(score)
