# 문제 1부터 50까지의 합을 구하기
# 단, while문이용

# num=1
# sum=0
# while num <= 50:
#     sum = sum+num
#     num = num+1

# print(sum)
    
# 다중 while문을 이용해서 구구단 2단~9단까지 출력

j = 2
while j <= 9:
    i = 1
    while i <= 9:
        print(f"{j} * {i} = {j*i}")
        i += 1    
    j += 1