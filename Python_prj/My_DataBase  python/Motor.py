class Motor:
    Motor={}
    def __init__(self):
        self.Motor={'X좌표':0,'Y좌표':0,'Z좌표':0,'Rpm':0,'각도':0}
        self.Setting()

    def Setting(self):
        for key in self.Motor.keys():
            print(key,end='')
            Value=input('의 값 입력: ')
            self.Motor[key]=Value
        print("\n설정완료", "-"*65, "\n", self.Motor)
        return

# My_dict={}
# Key=input("Key 입력: ")
# Value=input("Value 입력: ").split()
# My_dict[Key]=Value
# print(My_dict)

    def Move(self):
        print("\n\nMotor_Move!\n"*10)
        print("\nMptor_Current_position:",
              '\nX좌표: ',self.Motor['X좌표'],
              '\nY좌표: ',self.Motor['Y좌표'],
              '\nZ좌표: ',self.Motor['Z좌표'],)
        return

    def Home(self):
        print("Motor_Move_Home!")
        return

    def m_delay(self, ms):
        print()
        print("-"*70)
        print()
        print('Delay\n'*ms)
        return
    
    def TXT_prt(self):
        file=open('Moto_Setting.txt','w')
        file.write('Moto_Setting'+('-'*40)+'\n')
        for key, val in self.Motor.items():
            file.write(f'{key}: {val}, ')
        file.close()
        return
pass