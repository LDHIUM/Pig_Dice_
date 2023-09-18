bank = 0
while True:
    start = input('주사위를 던지려면 엔터를 누르세요: ')
    a = dice()
    if a == 1:
        print('1이 나왔습니다.')
        break
    else:
        print(f"A의 주사위는 {a} 입니다. ")
        bank += a
        if bank >= 50:
            print('bank가 50이 넘었습니다. 승리하였습니다.')
        else:
            print(f"Bank는 {bank}입니다.")
