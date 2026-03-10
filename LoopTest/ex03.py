select = 0
insert = 0
update = 0
delete = 0

while True:
    # .upper() => input에서 소문자를 입력해도 대문자로 들어감
    # .lower() => input에서 대문자를 입력해도 소문자로 들어감
    queryType = input("쿼리 유형 입력: ").upper()

    if queryType == "EXIT":
        break        
    elif queryType == "SELECT":
        select += 1
        continue
    elif queryType == "INSERT":
        insert += 1
        continue
    elif queryType == "UPDATE":
        update += 1
        continue
    elif queryType == "DELETE":
        delete += 1
        continue
    elif queryType == "REPORT":
        print("--- 쿼리 실행 현황 ---")
        print(f"SELECT : {select}회")
        print(f"INSERT : {insert}회")
        print(f"UPDATE : {update}회")
        print(f"DELETE : {delete}회")
        # 횟수총합
        total = select+insert+update+delete     
        print(f"총 실행 : {total}회")
    
        # select 퍼센트계산
        percent = (select/total)*100
        if(percent >= 70):
            print(f"SELECT 비율 : {percent}%")
            print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")
        continue
    else:
        print("알 수 없는 쿼리 유형입니다.")
        continue

# EXIT후 실행
print("--- 쿼리 실행 현황 ---")
print(f"SELECT : {select}회")
print(f"INSERT : {insert}회")
print(f"UPDATE : {update}회")
print(f"DELETE : {delete}회")
# 횟수총합
total = select+insert+update+delete     
print(f"총 실행 : {total}회")

# select 퍼센트계산
percent = (select/total)*100
if(percent >= 70):
    print(f"SELECT 비율 : {percent}%")
    print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")