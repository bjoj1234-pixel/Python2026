name = input("이름을 입력하세요:")
height = float(input("키를 입력하세요(cm):"))
weight = float(input("현재 체중을 입력하세요(kg):"))

standard = (height - 100)*0.9
fat = weight/standard * 100


print("-"*60)

print(f"{name}의 비만도는 {fat:.2f}%입니다.")

print("-"*60)
