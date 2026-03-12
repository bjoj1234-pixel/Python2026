# default 매개변수 지정하기
# 파이썬은 매개변수에 기본값을 지정할 수 있다.
# 이것을 default argument라 한다.

def greet(name,msg='별일 없죠'):
    print(f'안녕 {name} {msg}')

greet('개나리')
# -> 안녕 개나리 별일 없죠
greet('개나리','별일 있죠')
# -> 안녕 개나리 별일 있죠(기본값을 저장했어도 변경가능)