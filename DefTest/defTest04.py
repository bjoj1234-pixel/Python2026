# 파이썬의 함수는 return 여러개 받을 때
# -> 튜플을 사용한다.

def cal(a,b):
    sum_def = a + b
    diff_def = a - b
    return (sum_def, diff_def) #튜플로 묶어서 반환
# 함수호출
s,d = cal(10,5)
print(f"합: {s}, 차: {d}")