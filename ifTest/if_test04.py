# 문제)
# 연도가 4로 나누어 떨어지면 윤년이나, 100으로 나누어 떨어지는 연도는 제외한다.

year = int(input("연도를 입력하세요"))

if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")