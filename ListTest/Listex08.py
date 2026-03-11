# 성적표
report = [
    {'subject': 'Phython프로그래밍\t', 'score': 92, 'credit': 3},
    {'subject': 'SpringBoot 개발\t\t', 'score': 88, 'credit': 3},
    {'subject': 'React 프론트엔드\t', 'score': 76, 'credit': 2},
    {'subject': '데이터베이스\t\t', 'score': 95, 'credit': 3},
    {'subject': '알고리즘\t\t', 'score': 68, 'credit': 2}
]


print("=== 성적표 ===")

print("과목\t\t\t점수\t학점\t학점포인트\t이수학점")
print("-----------------------------------------------------------------")


# 학점포인트 * 이수학점
complete = 0
# 이수학점 총계
total = 0
# 학점분포배열
grade = {'A+': 0,'A': 0,'B+': 0,'B+': 0,'C+': 0,'C': 0,'D': 0,'F': 0}

for i in range(len(report)):
    print(f"{report[i]['subject']}{report[i]['score']}점\t", end =" ")

    
    if report[i]['score'] >= 95:
        report[i]['distribution'] = 'A+'
        report[i]['scorePoint'] = 4.5
        grade['A+'] += 1
    elif report[i]['score'] < 95 and report[i]['score'] >= 90 :
        report[i]['distribution'] = 'A'
        report[i]['scorePoint'] = 4.0
        grade['A'] += 1
    elif report[i]['score'] < 90 and report[i]['score'] >= 85 :
        report[i]['distribution'] = 'B+'
        report[i]['scorePoint'] = 3.5
        grade['B+'] += 1
    elif report[i]['score'] < 85 and report[i]['score'] >= 80 :
        report[i]['distribution'] = 'B'
        report[i]['scorePoint'] = 3.0
        grade['B'] += 1
    elif report[i]['score'] < 80 and report[i]['score'] >= 75 :
        report[i]['distribution'] = 'C+'
        report[i]['scorePoint'] = 2.5
        grade['C+'] += 1
    elif report[i]['score'] < 75 and report[i]['score'] >= 70 :
        report[i]['distribution'] = 'C'
        report[i]['scorePoint'] = 2.0
        grade['C'] += 1
    elif report[i]['score'] < 70 and report[i]['score'] >= 60 :
        report[i]['distribution'] = 'D'
        report[i]['scorePoint'] = 1.0
        grade['D'] += 1
    else:
        report[i]['distribution'] = 'F'
        report[i]['scorePoint'] = 0
        grade['F'] += 1

    # 학점포인트 * 이수학점
    complete += (report[i]['scorePoint']*report[i]['credit'])
    # 이수학점 총계
    total += report[i]['credit']
    print(f"{report[i]['distribution']}\t{report[i]['scorePoint']}\t\t{report[i]['credit']}학점")

print()
# GPA
avg = complete/total
print(f"GPA: {avg:.2f} / 4.50  (총 13학점)")
print()

print(f"학점 분포: {grade}")