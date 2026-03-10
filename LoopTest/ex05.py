# 측정횟수입력
num = int(input("측정횟수 : "))

# 총합계
total = 0
#총 횟수
totalNum = 0
#크리티컬 횟수
criNum = 0

for i in range(num):

    time = int(input(f"응답시간 {i+1} (ms):"))

    if i == 0:
        max = time
        min = time
    else:
        # 최대값 및 최소값 저장
        if max < time:
            max = time

        if min > time:
            min = time

    if time <= 100:
        print("FAST")
    elif time >= 101 and time <= 300:
        print("NORMAL")
    elif time >= 301 and time <= 1000:
        print("SLOW")
    else:
        print("CRITICAL")
        criNum += 1

    total += time    
    totalNum += 1


# 평균
avg = total/num
print(f"평균 응답시간: {avg}ms")    
print(f"최대: {max}ms | 최소: {min}ms")    

cripercent = (criNum/totalNum)*100

if cripercent >=10:
    print("SLA 위반! 서버 점검이 필요합니다")
