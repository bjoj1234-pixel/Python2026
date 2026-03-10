# a=[1,2,3,4,5] => 리스트, 일종의 배열과 같은 의미

# i=1,i=2,i=3,i=4,i=5
for i in [1,2,3,4,5]:
    print("반복문")

# for 변수 in range(종료값) => 변수가 0부터 종료값 -1까지 반복됨
for i in range(5):
    print(f"range-{i}까지 반복")

# for 변수 in range(초기값, 종료값, 증감값)
# 1부터 5까지 반복하여 숫자출력
# 1~5까지 돌리려면 6에서 끝나야 되므로 종료값 6을 넣어줌
for i in range(1,6,1):
    print(f"{i}")

# 다중 for문을 이용해서 구구단 2단~9단 출력
for i in range(2,10,1):
    print(f"----{i}단 시작----")

    for j in range(1,10,1):
        print(f"{i}X{j}={i*j}")
        
    #한단이 끝날때마다 빈줄출력
    print()