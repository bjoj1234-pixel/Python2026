orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'}
]
# 합계금액
total = 0
# 새 배열
carts = []

print("=== 결제 완료 주문 ===")
for i in range(len(orders)):
    if orders[i]['status'] == 'PAID':
        # 총 결제금액 누적
        total += orders[i]['amount']
        # 카트에 담기
        carts.append(orders[i])

for cart in carts:
    print(f"{cart['id']}번 주문 / 상품 : {cart['product']} / {cart['amount']:,}원")

print()     
print(f"총 결제 금액: {total:,}원")


