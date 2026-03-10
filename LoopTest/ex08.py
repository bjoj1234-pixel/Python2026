# 목표 일 매출액
target = int(input("목표 일 매출액: ") )

# 총매출
total = 0
# 목표달성
success = 0

# for문 돌려 요일별 목표여부 출력
for i in range(7):
    if i == 0:
        day = "월"
    elif i == 1:
        day = "화"
    elif i == 2:
        day = "수"
    elif i == 3:
        day = "목"
    elif i == 4:
        day = "금"
    elif i == 5:
        day = "토"
    else:        
        day = "일"

    # 요일 매출 입력
    sell = int(input(f"{day}요일 매출: ") )

    if i == 0:
        max = sell
        maxDay = ""
        min = sell
        minDay = ""
    else:
        # 최대값 및 최소값 저장
        if max < sell:
            max = sell
            maxDay = day

        if min > sell:
            min = sell
            minDay = day

    if sell >= target:
        print("→ 목표 달성")
        # 목표달성누적
        success += 1
    elif target > sell and sell >= target*0.7:
        print("→ 분발 필요")
    else:
        print("→ 목표 미달")

    # 총 매출누적
    total += sell

print(f"총 매출: {total:,}원 | 일평균: {int(total/7):,}원")
print(f"최고 매출: {maxDay}요일 {max:,}원 | 최저 매출: {minDay}요일 {min:,}원")
print(f"목표 달성: {success}일")

    


