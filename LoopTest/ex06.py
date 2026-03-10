#if grade not in [1,2,3,4,5] ==> 1~5를 제외한

# 주문건수
cnt = 0
# 총 금액
totalPrice = 0
# 총 할인
totalSale = 0

while True:
    grade = input("회원 등급 (END 종료): ").upper()
    
    # 할인퍼센트
    sale = 0
    # 추가할인금액
    addSale = 0
    # 계산금액
    calcPrice = 0   
    
    if grade == "BRONZE":
        sale = 0
    elif grade == "SILVER":
        sale = 0.05
    elif grade == "GOLD":
        sale = 0.1
        addSale = 5000
    elif grade == "VIP":
        sale = 0.2
        addSale = 10000
    elif grade == "END":
        break
    else:
        print("등록되지 않은 등급입니다. 다시 입력해주세요")
        continue

    price = int(input("구매금액: "))

    # 주문건수 증가
    cnt += 1

    # 결제금액 계산
    calcPrice = int(price - (price*sale) - addSale)
    print(f"할인금액: {int(price*sale + addSale):,}원 → 결제금액: {calcPrice:,}원")
    
    # 총 결제금액 누적
    totalPrice += calcPrice
    # 총 할인누적
    totalSale += price*sale + addSale

print("--- 전체 주문 요약 ---")
print(f"주문 건수 : {cnt}건")
print(f"총 구매금액 : {int(totalPrice + totalSale):,}원 | 총 할인 : {int(totalSale):,}원 | 총 결제 : {int(totalPrice):,}원")