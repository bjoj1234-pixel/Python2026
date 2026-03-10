movieNum = "2026-0309-01"
movieStation = "7관 (4층)"
movieTitle = "파이썬의 습격"
movieTime = "14:30 ~ 16:10"

normalPrice = 15000
normalNum = 2
studentPrice = 10000
studentNum = 1
total = normalPrice*normalNum + studentPrice*studentNum

print("=" * 60)
print(f"{"PYTHON CINEMA":>35}")
print("=" * 60)

print(f"티켓번호 : {movieNum}")
print(f"상영관 : {movieStation}")
print(f"영화명 : {movieTitle}")
print(f"상영시간 : {movieTime}")

print("-" * 60)
print(f"{"구분":<15} {"단가":>10} {"인원":>10} {"금액":>10}")
print("-" * 60)
print(f"{"일반성인:":<15} {normalPrice:>10,} {normalNum:>10,} {normalPrice*normalNum:>17,}")
print(f"{"청소년:":<15} {studentPrice:>11,} {studentNum:>10,} {studentPrice*studentNum:>17,}")
print("-" * 60)
print(f"{"총 결제 금액:":<45} {total:>,}")
print("=" * 60)
