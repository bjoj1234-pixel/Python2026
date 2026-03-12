transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]

# 월별 합산 빈 딕셔너리 생성
monthly_sales = {}

for date, amount in transactions:
    # monthly_sales에 이미 해당 월이 존재하면 금액 더 해준다
    if date in monthly_sales:
        monthly_sales[date] += amount
    else:
    # 처음 등장하는 월이면 금액을 넣는다.
        monthly_sales[date] = amount
        
print(monthly_sales)
# {'2024-01': 4700000, '2024-02': 3700000, '2024-03': 6300000, '2024-04': 5100000, '2024-05': 5000000, '2024-06': 2100000}

# 통계 계산을 위한 변수지정, 최소/최대
max_sales = 0
max_month = ""
min_sales = 0
min_month = ""
total = 0
print("==== 월별 매출 ====")

for month in monthly_sales:
    # 현재 monthly_sales의 값 {'2024-01': 4700000}
    # 딕셔너리 접근 방법 : 딕셔너리 이름['key이름']
    sales = monthly_sales[month]
    print(f"{month}: {sales:,}원")

    #총계 구하기
    total += sales

    # 최대값 & 최대값 월
    if max_month == "" or sales > max_sales:
        max_sales = sales
        max_month = month
    # 최소값 & 최소값 월
    if min_month == "" or sales < min_sales:
        min_sales = sales
        min_month = month

# 월평균 구하기
avg = total / len(monthly_sales)

#출력문
print("-"*35)
print(f"최고 매출 월:{max_month} {max_sales:,}원")
print(f"최저 매출 월:{min_month} {min_sales:,}원")
print(f"월 평균 매출:{avg:,.2f}원")



