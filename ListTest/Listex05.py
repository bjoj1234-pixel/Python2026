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

print("=== 월별 매출 ===")
monthArray = transactions

for i in range(len(transactions)):
    for j in range(len(transactions[i])):
        # 년-월만 필터
        if j % 2 == 0:
            # if monthArray[i][j] == transactions[i][j]:                
            #     monthArray['month'] += transactions[i][1]
            # else:
            #     monthArray['month'] = transactions[i][1]


            
            print(monthArray)
