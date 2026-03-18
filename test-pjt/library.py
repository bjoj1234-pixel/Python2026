from datetime import datetime, timedelta

# 도서 목록
books = [
    {'id':'B001','title':'파이썬 완전정복','author':'홍길동','genre':'IT','total':3,'available':2},
    {'id':'B002','title':'데이터분석 입문','author':'김데이터','genre':'IT','total':2,'available':2},
    {'id':'B003','title':'알고리즘의 이해','author':'이알고','genre':'IT','total':2,'available':1},
    {'id':'B004','title':'채식주의자','author':'한강','genre':'소설','total':4,'available':4},
    {'id':'B005','title':'82년생 김지영','author':'조남주','genre':'소설','total':3,'available':3}
]
# 대출 기록
loans = [
    {'loan_id':'L001','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
    {'loan_id':'L002','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False}
]

#도서 목록 조회
def show_books():
    print("도서ID\t제목\t\t저자\t장르\t전체\t가능\t상태")
    print("-"*70)
    for book in books:
        print(f"{book['id']}\t{book['title']}\t{book['author']}\t{book['genre']}\t{book['total']}\t{book['available']}\t", end=" ")
        if book['available'] > 0 :
            print("대출가능")
        else:
            print("대출불가")
    print()

# 기준 날짜 (연체 확인용)
today = '2025-06-10'
#1. 문자열 → 날짜로 변환
date_obj = datetime.strptime(today, '%Y-%m-%d')
#2. 14일 더하기
after_14 = (date_obj + timedelta(days=14)).strftime('%Y-%m-%d')

#도서 대출
def loan_book():
    memberName = input("회원명을 입력하세요: ")
    bookID = input("대출할 도서ID를 입력하세요: ").upper()
    # 책 존재여부
    exist = False

    for book in books:
        # 입력한 책id가 있으면
        if bookID in book['id']:
            exist = True #존재함

            if book['available'] == 0: # 가능한 수량이 0이면
                print("현재 대출 가능한 도서가 없습니다.")
            else: # 가능한 수량이 있으면

                # 대출목록에 저장
                if len(loans) < 10: #L00(숫자)
                    loans.append({'loan_id': 'L00'+str((len(loans)+1)), 'member':memberName, 'book_id': bookID, 'loan_date': today,
                                   'due_date': after_14, 'returned':False})
                elif len(loans) >= 10 and len(loans) < 100: #L0(숫자)
                    loans.append({'loan_id': 'L0'+str((len(loans)+1)), 'member':memberName, 'book_id': bookID, 'loan_date': today,
                                   'due_date': after_14, 'returned':False})
                else: #L(숫자)
                    loans.append({'loan_id': 'L'+str((len(loans)+1)), 'member':memberName, 'book_id': bookID, 'loan_date': today,
                                   'due_date': after_14, 'returned':False})
                
                #가능수량 1감소
                book['available'] = book['available']-1 
                print(f"[대출 완료] {memberName}님이 '{book['title']}'을(를) 대출하였습니다.\n")
                print(f"대출번호: {loans[len(loans)-1]['loan_id']} | 반납예정일: {loans[len(loans)-1]['due_date']}\n")
            break
        else:
            exist = False #존재안함
            
    if exist == False:
        print("등록되지 않은 도서입니다.\n")
        return
        
    
#대출 현황 조회
def show_loans():
    print("대출번호\t회원명\t도서제목\t대출일\t반납예정일\t반납여부")
    print("-"*70)

    for loan in loans:        
        print(f"{loan['loan_id']}\t{loan['member']}\t", end=" ")
        for book in books:
            if loan['book_id'] in book['id']:            
                print(f"{book['title']}\t", end=" ") # 도서제목 출력
        print(f"{loan['loan_date']}\t{loan['due_date']}\t", end=" ")
        if loan['returned'] == False:
            print("대출중")
        else:
            print("반납완료")
    print()


#도서 반납
def return_book():
    returnBook = input("대출번호를 입력하세요: ").upper()

    # 대출번호 존재여부
    exist = False

    for loan in loans:
        if returnBook in loan['loan_id']:

            if loan['returned'] == False: #반납 안한 상태면
                exist = True #대출번호 존재

                print("[반납 완료] ",end=" ")

                for book in books:
                    if loan['book_id'] in book['id']:            
                        print(f"{book['title']}\t", end=" ") # 도서제목 출력
                        book['available'] = book['available'] + 1 #가능 숫자 1증가

                print("이(가) 반납되었습니다.\n")

                loan['returned'] = True #반납함
                return

            else: #반납한 상태면
                print("이미 반납된 도서입니다.")
                return
                        
        else:            
            exist = False #대출번호 존재안함
    
    if exist == False:
        print("해당 대출 기록이 없습니다.\n")
        return


#연체현황 조회
def show_overdue():
    print(f"=== 연체 현황 (기준일: {today}) ===")
    print("대출번호\t회원명\t도서제목\t반납예정일")
    print("-"*70)

    # 연체건 존재여부
    exist = False

    for loan in loans:
        #반납을 안한상태면
        if loan['returned'] == False:
            # 반납일자를 문자열 → 날짜로 변환
            date_obj02 = datetime.strptime(loan['due_date'], '%Y-%m-%d')
            #반납일자가 오늘일자보다 이전이면
            if date_obj02 < date_obj:
                print(f"{loan['loan_id']}\t{loan['member']}\t", end=" ")
                
                for book in books:
                    if loan['book_id'] in book['id']:            
                        print(f"{book['title']}\t", end=" ") # 도서제목 출력

                print(loan['due_date'])
                exist = True #연체건 존재

    #연체건이 없으면
    if exist == False: 
        print("현재 연체된 도서가 없습니다.")
    print()


#장르별 통계
def show_genre_stats():
    print("장르\t전체권수\t대출중")
    print("-"*70)

    
    
    #장르별 출력을 위한 임시저장 리스트
    global genreList
    genreList = []

    for book in books:        
        # 리스트 존재여부
        exist = False

        for list in genreList:
            if list['genre'] in book['genre']:
                #이미 등록되있는 장르가 있으면
                list['total'] = int(list['total']) + int(book['total']) #토탈값 증가
                list['loan'] = int(list['loan']) + (int(book['total']) - int(book['available'])) #대출중 수 증가
                exist = True # 리스트 존재함

        if exist == False: #리스트에 없으면
            #등록되있는 장르가 없으면 새로 저장
            genreList.append({'genre': book['genre'], 'total':book['total'], 'loan': (int(book['total']) - int(book['available']))})

    for list in genreList:
        print(f"{list['genre']}\t{list['total']}\t{list['loan']}")



# 프로그램 실행
while True:
    print("=== 도서관 대출 관리 시스템===")
    print("1. 도서 목록 조회")
    print("2. 도서 대출")
    print("3. 도서 반납")
    print("4. 대출 현황 조회")
    print("5. 연체 현황 조회")
    print("6. 장르별 통계")
    print("0. 종료\n")

    menuSelect = int(input("메뉴를 선택하세요: "))

    if menuSelect == 1: #도서 목록 조회
        show_books()
    elif menuSelect == 2: #도서 대출
        loan_book()
    elif menuSelect == 3: #도서 반납
        return_book()
    elif menuSelect == 4: #대출 현황 조회
        show_loans() 
    elif menuSelect == 5: #연체 현황 조회
        show_overdue()
    elif menuSelect == 6: #장르별 통계
        show_genre_stats()
    elif menuSelect == 0: #종료
        print("\n프로그램을 종료합니다.")
        break
    else:
        print("\n메뉴를 잘못 입력하셨습니다. 다시 입력해주세요.\n")
        