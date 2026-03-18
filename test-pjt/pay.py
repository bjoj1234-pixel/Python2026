name = input("이름을 입력하세요: ")
wage = int(input("시급을 입력하세요(원): "))
fulltime = int(input("하루 근무 시간을 입력하세요(h): "))
workDay = int(input("근무 일수를 입력하세요(일): "))
startTime = int(input("근무 시작시간을 입력하세요(0~23): "))

print("=" * 70)
print(" 급여 명세서")
print("=" * 70)
print(f"이름 : {name}")
print(f"시급 : {wage:,}원")

# 총 근무시간(일주일)
totalTime = fulltime*workDay

print(f"근무시간 : {totalTime}시간 ({fulltime}h x {workDay}일)")

if startTime >= 22 or startTime <= 6:
    wage=14790
    basicSalary = totalTime*wage
    print(f"야간 근무 : 해당 있음 (시급 14,790원 적용)")
else:
    basicSalary = totalTime*wage
    print(f"야간 근무 : 해당 없음 (기본시급 적용)")

# 일주일 총 근무시간 15시간 이상일시
if totalTime >= 15:
    bonus = fulltime*wage
    # 총급여
    total = basicSalary + bonus
    #세금
    tax = total * 0.033
    print(f"주휴수당 : 해당 있음")
else:
    bonus = 0
    # 총급여
    total = basicSalary + bonus
    #세금
    tax = total * 0
    print(f"주휴수당 : 해당 없음")
print("=" * 70)
print(f"기본급 : {basicSalary:,}원")
print(f"주휴수당 : {bonus:,}원")

print(f"세금(3.3%) : {int(tax):,}원")
print("-" * 70)

print(f"실수령액 : {int(total-tax):,}원")
print("=" * 70)




