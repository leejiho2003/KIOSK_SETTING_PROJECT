money=int(input('돈을 넣어주세요 : '))
moca = 100
cocoa = 150

while True:
    if coffee>=1:
        choice=int(input('마시고 싶은 커피를 선택하세요\n1.모카\n2.코코아\n'))
        print(str(choice)+'를 선택했습니다')
        if choice == 1 and money>=moca :
            print('모카커피가 나왔습니다')
            coffee-=1
            money-=moca
        elif choice == 2 and money>=cocoa :
            print('코코아가 나왔습니다')
            coffee-=1
            money-=cocoa
        elif money<cocoa or money<moca:
            print('잔돈이 부족합니다')
        else :
            print('없는 메뉴입니다')
            continue
        print('잔돈은 '+str(money)+'원 입니다')
        choice = str(input('거스름돈을 받으려면 q를 누르고 계속 진행하려면 다른 키를 입력해주세요.')
        if choice == 'q':
            print('잔돈'+str(money)+"원이 나왔습니다")
            break
    else :
        print('커피가 부족합니다')
        break
