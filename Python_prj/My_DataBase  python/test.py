from Motor import Motor

def Main_exe():
    Motor1=Motor()

    Motor1.Move()
    Motor1.m_delay(10)
    Motor1.Home()
    Motor1.TXT_prt()
    return

Main_exe()

from random