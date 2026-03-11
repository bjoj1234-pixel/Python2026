# 리스트 = 배열과 같은 역할을 한다.
# 리스트 [숫자, 문자, 혼합] 사용가능
# 동적 => 고정길이가 아님
# 단, 속도는 조금 느림

heroes = []
# 리스트 추가하는 방법
# append('추가할 문자') => 맨 뒤에 추가
# insert(인덱스번호, '추가 문자') => 인덱스 번호에 추가

heroes.append('아이언맨')
heroes.append('닥터 스트레인지')
print(heroes)
# => ['아이언맨', '닥터 스트레인지']

heroes.insert(1, '왕과 사는 남자')
print(heroes)
# => ['아이언맨','왕과 사는 남자', '닥터 스트레인지']

# 리스트 삭제 : remove('삭제할 문자')
# 리스트 삭제 : del heroes[0] => 0번째 데이터 삭제됨
# 리스트 삭제 : pop => 맨 마지막 데이터 삭제됨

heroes.remove('왕과 사는 남자')
print(heroes)
# => ['아이언맨', '닥터 스트레인지']

del heroes[1]
print(heroes)
# => ['아이언맨']

heroes.pop()
print(heroes)
# => []

heroes.append('a')
heroes.append('b')
heroes.append('c')
heroes.append('d')
print(heroes)

# for문을 이용해서 출력하기
for title in heroes:
    print(title, end=" ")

print()
# 리스트 슬라이스 하기
# heroes[0:3] => 0번째 부터 3글자
# heroes[:3] => 처음부터 3글자
# heroes[3:] => 세번째 글자부터 마지막까지
cut = heroes[0:2]
print(cut)
# => ['a', 'b']

cut2 = heroes[3:]
print(cut2)
# => ['d']

# 문제) movieTitle = []에 아래 영화 제목 4개를 추가하시오.
# 아이언맨, 토르, 헐크, 스칼렛 위치

movieTitle=[]

movieTitle.append('아이언맨')
movieTitle.append('토르')
movieTitle.append('헐크')
movieTitle.append('스칼렛 위치')

for movie in movieTitle:
    print(movie, end="  ")

# 문제) movieTitle에서 '토르'가 존재하면 삭제하고 출력할 것

print()

if '토르' in movieTitle:
    movieTitle.remove('토르')

movieTitle.sort(reverse=True)
# 내림차순 정렬

for movie in movieTitle:
    print(movie, end="  ")
