response = {
    'code' : 200,
    'message': 'success',
    'data' 
    : [
        {'userId': 'user01', 'name': '이자바', 'score': 95},
        {'userId': 'user02', 'name': '박리액트', 'score': 82},
        {'userId': 'user03', 'name': '최스프링', 'score': 91},
        {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
    ]
}

print("=== 전체 성적 ===")

# 우수인원
great = {}

if response['code'] == 200:
    for data in response['data']:
        print(f"{data['name']} ({data['userId']}): {data['score']}점")
        if data['score'] >= 90:
            name = data['name']
            score = data['score']
            
            if name in great:
                continue
            else:
                great[name] = score

print()
print("=== 우수 수강생 (90점 이상) ===")

for key in great.keys():
    print(f"★  {key}: {great[key]}점")



