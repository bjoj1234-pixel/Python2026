
books = [("파이썬 기초", 15000), ("자바의 정석", 25000), ("React 입문", 18000)]

total = 0

def total_price():
    print("---- 도서 목록 ----")
    for title,price in books:
        print(f"도서명: {title}, 가격: {price:,}원")
        global total
        total += price
    print()
    print(f"전체 도서 합계: {total:,}원")


total_price()