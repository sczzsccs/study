import random as rd
import time

R_Bit = 1024
print(bin(R_Bit))
while True:
    R_int = rd.randint(-999, 1000)
    # -999 ~ 1000 범위에서 '=='만 사용하여 음수 찾기
    if int(R_int & R_Bit) == 1024: print(R_int, "음수")
    else: print(R_int)
    time.sleep(0.3)