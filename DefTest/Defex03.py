member_data = [
    {"name": "김철수", "age": 20},
    {"name": "이영희", "age": 25},
    {"name": "박민수", "age": 18}
]

ageFilter = []

def filter_members():
    for member in member_data:
        if member["age"] >= 20:
            ageFilter.append(member["name"])
    print(f"20세 이상 회원: {ageFilter}")

filter_members()