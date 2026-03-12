rooms = [
    {'id': 101, 'name': '스탠다드 A' ,'price': 100000, 'max': 2, 'status': True},
    {'id': 102, 'name': '스탠다드 B' ,'price': 110000, 'max': 2, 'status': True},
    {'id': 201, 'name': '디럭스 룸 A' ,'price': 250000, 'max': 3, 'status': False},
    {'id': 202, 'name': '디럭스 룸 B' ,'price': 300000, 'max': 4, 'status': True},
    {'id': 301, 'name': '스위트 룸 A' ,'price': 500000, 'max': 4, 'status': True},
    {'id': 302, 'name': '스위트 룸 B' ,'price': 550000, 'max': 4, 'status': False}
]

# 객실현황 보기
def show_rooms(status):
    print("="*60)
    print("ID\t객실명\t\t가격\t\t최대인원\t상태")
    print("-"*60)
    
    # 모두보기
    if status == False:
        for room in rooms:
            print(f"{room["id"]}\t{room["name"]}\t{room["price"]:,}원\t{room["max"]}\t",end="")
            if room["status"] == True:
                print("예약가능")
            else: 
                print("예약불가")

    else: # 예약 가능상태인 룸만 보기
        for room in rooms:
            if room["status"] == True:
                print(f"{room["id"]}\t{room["name"]}\t{room["price"]:,}원\t{room["max"]}\t",end="")
                if room["status"] == True:
                    print("예약가능")
                else: 
                    print("예약불가")
        
    print("="*60)

# 예약내역
reservations = []

# 방 별 비용계산 함수
def calculate_price(room_id, days, people):
    # 예약한 방값 초기화
    totalPrice = 0

    for room in rooms:
        # 입력한 id 방의 방값 X 일수
        if room_id == room['id']:
            totalPrice = room['price']*days
            # 인원 초과시 인당 20000원씩 추가
            if people > room['max']:
                totalPrice += ((people - room['max']) * 20000)
        
    # 최종금액반환
    return totalPrice


# 예약 함수
def make_reservation(room_id, guest_name, people, days):
    print()

    # 예약 성공여부
    isSuccess = False
    
    for room in rooms:
        # 입력한 id와 일치한게 있으면
        if room_id == room['id']:
            isSuccess = True # 예약 성공여부 true
            room['status'] = False # 예약상태를 불가로 바꿈
            # 객실 비용계산
            totalPrice = calculate_price(room_id, days, people)
            # 예약리스트에 추가
            reservations.append({'id': room_id, 'name':guest_name, 'people': people, 'totalPrice': totalPrice})
            print(f"[성공] {guest_name}님, {room_id}호 예약이 완료되었습니다.")
            return
    

    if isSuccess == False:
        print("객실번호를 다시 확인해주세요.")
    print()   
        

# 전체 예약내역 및 매출확인
def totalReport():
    total = 0
    print() 
    print("--- 전체 예약 명단 ---")
    for reserv in reservations:
        print(f"객실번호: {reserv['id']}호 | 성함: {reserv['name']} | 인원: {reserv['people']}명 | 결제금액: {reserv['totalPrice']:,}원")
        total += reserv['totalPrice']

    print(f"현재 확정 매출 합계: {total:,}원")
    print()

# 삭제함수
def cancel_reservation(room_id):
    # 삭제 성공여부
    isSuccess = False

    for reserv in reservations:
        if room_id == reserv['id']:            
            #예약 내역삭제
            reservations.remove(reserv)
            
            for room in rooms:
                if room_id == room['id']:
                    room['status'] = True #삭제한 예약 내역은 다시 예약가능하게
            isSuccess = True #삭제 성공여부
    #삭제 실패시
    if isSuccess == False:
        print("입력한 객실번호를 다시 확인해주세요.")
    print()  

while True:
    print("--- 리조트 예약 관리 시스템 ---")
    print("1. 객실 현황 보기")
    print("2. 객실 예약하기")
    print("3. 예약 내역 및 매출 확인")
    print("4. 예약 내역 삭제")
    print("5. 프로그램 종료")
    
    selectMenu = int(input("원하는 메뉴 번호를 선택하세요: "))

    if selectMenu == 1: #객실현황보기
        show_rooms(False) #객실 목록 모두출력

    elif selectMenu == 2: #객실예약하기
        show_rooms(True) #객실가능한 목록 출력
        room_id = int(input("예약할 객실 번호를 입력하세요: "))
        guest_name = input("예약자 성함을 입력하세요: ")
        people = int(input("투숙 인원을 입력하세요: "))
        days = int(input("숙박일수를 입력하세요: "))
        # 예약함수실행
        make_reservation(room_id, guest_name, people, days)

    elif selectMenu == 3: #예약내역 및 매출 확인
        totalReport() #예약된 목록출력

    elif selectMenu == 4: #예약 내역 삭제
        totalReport() #예약된 목록출력
        room_id = int(input("삭제할 객실 번호를 입력하세요: "))
        # 삭제함수 실행
        cancel_reservation(room_id)
    elif selectMenu == 5: #프로그램 종료
        print("프로그램을 종료합니다. 수고하셨습니다.")
        break
    else:
        print("메뉴를 잘못입력했습니다. 다시 입력해주세요.")
