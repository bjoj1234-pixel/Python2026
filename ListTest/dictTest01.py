# 딕셔너리 = 오브젝트이다.
# 딕셔너리 => key : value가 쌍으로 존재한다.
# 딕셔너리 출력하는 방법
# dict['key']로 출력한다(절대 dict.key로 출력할 수 없다.)
# phone_book = {'name': '홍길동', 'age': 7, 'class': '고급'}
phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
phone_book['강감찬'] = '010-1234-5679'
phone_book['이순신'] = '010-1234-5670'

# 모두 출력
print(phone_book)
# key만 출력
print(phone_book.keys())
# 값만 출력
print(phone_book.values())

# 문제) phone_book을 강감찬 010-1234-5679 이렇게 출력하시오(단,for문 사용)

for keyName in phone_book.keys():
    print(keyName, phone_book[keyName])