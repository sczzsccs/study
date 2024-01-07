from SmartHome import*

def Select():
    Home.report()
    print(
        "\n[1] 문 열기",
        "\n[2] 문 닫기",
        "\n[3] 창문 열기",
        "\n[4] 창문 닫기",
        "\n[5] 에어컨 켜기",
        "\n[6] 에어컨 끄기",
        "\n[7] 보일러 켜기",
        "\n[8] 보일러 끄기")
    try:
        return Action(int(input("명령: ")))
    except:
        print("잘못된 입력", end="")
        return 0

def Action(N:int):
    print()
    if(N==1):
        Home.PartiMedi["door"].Open()
        action = Home.PartiMedi["door"].strPrint()
    elif(N==2):
        Home.PartiMedi["door"].Close()
        action = Home.PartiMedi["door"].strPrint()
    elif(N==3):
        Home.PartiMedi["window"].Open()
        action = Home.PartiMedi["window"].strPrint()
    elif(N==4):
        Home.PartiMedi["window"].Close()
        action = Home.PartiMedi["window"].strPrint()
    elif(N==5):
        Home.PartiMedi["aircon"].On()
        action = Home.PartiMedi["aircon"].strPrint()
    elif(N==6):
        Home.PartiMedi["aircon"].Off()
        action = Home.PartiMedi["aircon"].strPrint()
    elif(N==7):
        Home.PartiMedi["boiler"].On()
        action = Home.PartiMedi["boiler"].strPrint()
    elif(N==8):
        Home.PartiMedi["boiler"].Off()
        action = Home.PartiMedi["boiler"].strPrint()
    else:
        print("Error! 잘못된 명령", end="")
        return 0
    print(f"실행된 명령: {action}")
    return 1

Home = SmartHome()
while(Select()):
    pass
print("  .....프로그램 종료")