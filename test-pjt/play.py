adultPrice = 55000
studentPrice = 40000
childrenPrice = 28000
oldmanPrice = 15000



month = int(input("방문 월을 입력하세요(1~12): "))
adult = int(input("성인 인원수를 입력하세요: "))
student = int(input("청소년 인원수를 입력하세요: "))
children = int(input("어린이 인원수를 입력하세요: "))
oldman = int(input("경로 인원수를 입력하세요: "))


#총인원
peopleNum = adult+student+children+oldman


print("=" * 70)
print(" 놀이공원 입장권 계산서")
print("=" * 70)

print(f"방문 월 : {month}월")

# 성수기(7,8월)
if month == 7 or month == 8:
    sale = 0
    print("-- 성수기, 할인 미적용 --")
else:
    sale = 0.1
    print("-- 비수기 10%할인 적용 --")

print("=" * 70)

if peopleNum >=5 and children <3 :
    # 총비용 = 인원X비용
    adultTotal = adult * adultPrice
    studentTotal = student * studentPrice
    childrenTotal = children * childrenPrice
    oldmanTotal = oldman * oldmanPrice
    # 총 비용합계
    totalPrice = adultTotal+studentTotal+childrenTotal+oldmanTotal

    print(f"성인 {adult}명 : {adultTotal:,}원")
    print(f"청소년 {student}명 : {studentTotal:,}원")
    print(f"어린이 {children}명 : {childrenTotal:,}원")
    print(f"경로 {oldman}명 : {oldmanTotal:,}원")
    print("=" * 70)
    print(f"소계 : {totalPrice:,}원")
    print(f"단체할인 : -{int(totalPrice*sale):,}원")
    print("-" * 70)
    print(f"최종금액 : -{int((totalPrice - (totalPrice*sale))):,}원")
elif peopleNum >=5 and children >=3 :
     # 총비용 = 인원X비용
    adultTotal = adult * adultPrice
    studentTotal = student * studentPrice
    childrenTotal = children * 0
    oldmanTotal = oldman * oldmanPrice
    # 총 비용합계
    totalPrice = adultTotal+studentTotal+childrenTotal+oldmanTotal

    print(f"성인 {adult}명 : {adultTotal:,}원")
    print(f"청소년 {student}명 : {studentTotal:,}원")
    print(f"어린이 {children}명 : 0원 (무료!)")
    print(f"경로 {oldman}명 : {oldmanTotal:,}원")
    print("=" * 70)
    print(f"소계 : {totalPrice:,}원")
    print(f"단체할인 : -{int(totalPrice*sale):,}원")
    print("-" * 70)
    print(f"최종금액 : -{int((totalPrice - (totalPrice*sale))):,}원")
elif peopleNum <5 and children <3 :
     # 총비용 = 인원X비용
    adultTotal = adult * adultPrice
    studentTotal = student * studentPrice
    childrenTotal = children * childrenPrice
    oldmanTotal = oldman * oldmanPrice
    # 총 비용합계
    totalPrice = adultTotal+studentTotal+childrenTotal+oldmanTotal

    print(f"성인 {adult}명 : {adultTotal:,}원")
    print(f"청소년 {student}명 : {studentTotal:,}원")
    print(f"어린이 {children}명 : {childrenTotal:,}원")
    print(f"경로 {oldman}명 : {oldmanTotal:,}원")
    print("=" * 70)
    print(f"소계 : {totalPrice:,}원")
    print(f"단체할인 : 0원")
    print("-" * 70)
    print(f"최종금액 : {int(totalPrice):,}원")
else:
     # 총비용 = 인원X비용
    adultTotal = adult * adultPrice
    studentTotal = student * studentPrice
    childrenTotal = children * 0
    oldmanTotal = oldman * oldmanPrice
    # 총 비용합계
    totalPrice = adultTotal+studentTotal+childrenTotal+oldmanTotal

    print(f"성인 {adult}명 : {adultTotal:,}원")
    print(f"청소년 {student}명 : {studentTotal:,}원")
    print(f"어린이 {children}명 : 0원 (무료!)")
    print(f"경로 {oldman}명 : {oldmanTotal:,}원")
    print("=" * 70)
    print(f"소계 : {totalPrice:,}원")
    print(f"단체할인 : 0원")
    print("-" * 70)
    print(f"최종금액 : {int(totalPrice)}원")

print("=" * 70)
print(f"총 인원 : {peopleNum}명")
print("=" * 70)