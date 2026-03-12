menu = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}

def order_coffee(name,num=1):
    global menu
    if name in menu.keys():
        print(f"{name} {num}잔 주문 완료. 총액: {(num*menu[name]):,}원")
    else:
        print(f"죄송합니다. {name} 메뉴는 준비되어 있지 않습니다.")


order_coffee('아메리카노',3)
order_coffee('라떼')
order_coffee('에이드',2)
order_coffee('녹차',2)