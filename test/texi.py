# 출발지
startPoint = input("출발지를 입력하세요: ")
# 목적지
endPoint = input("목적지를 입력하세요: ")
# 이동거리
distance = float(input("이동거리(km)를 입력하세요: "))
# 탑승시간
boarding = int(input("탑승시간을 입력하세요(0~23 정수): "))
# 어린이 동반여부
children = int(input("어린이 동반여부(0번)동반X, 1번)동반O : "))


print("=" * 70)
print("택시 요금 안내")
print("=" * 70)

print(f"출발지 : {startPoint}")
print(f"목적지 : {endPoint}")
print(f"이동거리 : {distance}km")
print(f"탑승시간 : {boarding}시")

print("=" * 70)

#어린이 동반안하면
if children == 0:
    #기본요금
    basicPrice = 4800
else:
    basicPrice = 0

print(f"기본요금 : {basicPrice:,}원")

if distance>2:
    #거리요금
    distancePrice = int((distance-2)*1000)
else:
    distancePrice = 0

print(f"거리요금 : {distancePrice:,}원")

# 시간이 4~22이면(할증시간)
if boarding <= 4 or boarding >=22:
    # 최종요금
    extraCharge = int((basicPrice + distancePrice)*0.2)
else:
    extraCharge = 0

print(f"심야할증 : {extraCharge:,}원")

print("-" * 70)

total = int(basicPrice + distancePrice + extraCharge)

print(f"최종요금 : {total:,}원")

print("=" * 70)