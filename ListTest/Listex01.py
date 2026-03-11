products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]


print("== 재고 현황 ==")
for i in range(len(products)):   
    product = products[i]
    stock = stocks[i]
    # 파이썬은 문자와 숫자를 하나로 나열할 수 없다.
    # 그러므로 str()함수를 이용해 숫자를 문자열로 변환하여 나열한다.
    msg = product + ":" + str(stock) + "개"
    
    # 요즘은 아래와 같이 f-string쓰면 해결됨
    # print(f"{products[i]}: {stocks[i]}개",end=" ")

    if stock < 10:
        msg += ' 재고부족 '

    print(msg,end=" ")
    print()

total = 0
for stock in stocks: 
    total += stock
print()
print(f"전체 재고 합계 : {total:,}개")