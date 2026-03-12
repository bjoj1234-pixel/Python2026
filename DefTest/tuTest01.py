# 튜플이란 여러개의 데이터를 순서대로 저장
# 단, 수정/삭제/추가 안됨
# a = (10,20,30)
# 튜플접근 => a[0]

a = (10,20,30)

print(a[0])

# a[0] = 15
# 이미 저장되있는 값 수정 불가능

fruit = ('apple','banana','orange')

for f in fruit:
    print(f, end=" ")
print()
if 'abcd' in fruit:
    print("O")
else:
    print("X")

# 튜플은 괄호()가 없어도 된다.
t = 10,20,30
print(t)

# 문제 : 주어진 자료를 이용하여 합계, 평균 구하기
score = (80,50,75,90)
# 합계
total = 0

for s in score:
    total += s

# 평균
avg = total/len(score)

print(f"총합계:{total}, 평균:{avg}")


