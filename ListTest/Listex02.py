member = {
    'name' : '김파이썬',
    'email' : 'python@example.com',
    'age' : 28,
    'grade' : 'GOLD'
}

print("== 회원정보 ==")
for key in member.keys():
    print(f"{key}: {member[key]}")

    
print("연령 구간: ",end=" ")
if member['age'] < 20:
    print("주니어")
elif member['age'] >= 20 and member['age'] < 40:
    print("일반")
else:
    print("시니어")

print("전화번호: ",end=" ")

if 'phone' in member.keys():
    print(member['phone'])
else:
    print("미등록")



            

