import sys, os, random

from PyQt5 import QtCore, QtGui, QtWidgets
import Image.image_rc

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MpltCanvas(FigureCanvasQTAgg):
    def __init__(self):
        #글꼴
        matplotlib.rc('font', family='Malgun Gothic')
        fig = Figure()
        self.axis = fig.add_subplot()
        super(MpltCanvas, self).__init__(fig)
        pass
    pass

class User():
    def __init__(self) -> None:
        self.Upgrade_Target_Value = None
        self.Target_Goal_Times = None
        pass
    pass

# UI MAIN
class Ui_Dialog(object):
    def __init__(self) -> None:
        # Upgrade Percent List
        self.Up_Per=       [9500, 9000, 8500, 8500, 8000,
                            7500, 7000, 6500, 6000, 5500,
                            5000, 4500, 4000, 3500, 3000,
                            3000, 3000, 3000, 3000, 3000,
                            3000, 3000,  300,  200,  100]
        self.St_Up_Per=    [9975, 9450, 8925, 8925, 8400,
                            7875, 7350, 6825, 6300, 5775,
                            5250, 4725, 4200, 3675, 3150,
                            3150, 3150, 3150, 3150, 3150,
                            3150, 3150,  315,  210,  105]
        
        self.Down_per=     [0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000, 6790, 6790, 6720, 6720,
                            0000, 6300, 7760, 6860, 5940]
        self.St_Down_per=  [0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000, 6645, 6645, 6576, 6576,
                            0000, 6165, 7748, 6853, 5937]

        self.break_Per=    [0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            210 ,  210,  210,  280,  280,
                            700 ,  700, 1940, 2940, 3960]
        self.st_break_Per= [0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            0000,    0,    0,    0,    0,
                            206 ,  206,  274,  274,  274,
                            685 ,  685, 1937, 2937, 3958]
        
        self.upgrade_percent=self.Up_Per[0]
        self.Donwgrade_percent=self.Down_per[0]
        self.Break_percenot=self.break_Per[0]

        # Upgrade Manual Init
        self.Manual_Init_()

        # Upgrade Auto Init
        self.Auto_Init_()

        # Graph Plot, Figure Init
        self.Auto_Fail_Graph = MpltCanvas()
        self.Auto_Break_Graph = MpltCanvas()
        self.Auto_Fail_stats_Graph = MpltCanvas()
        self.Auto_Break_stats_Graph = MpltCanvas()
        self.Upgrad_Auto_Graph_Init()
        pass

    def Manual_Init_(self):
        self.M_Current_enforce = 0
        self.M_Next_enforce = self.M_Current_enforce + 1

        self.M_upgrade_percent = self.upgrade_percent=self.Up_Per[0]
        self.M_Donwgrade_percent = self.Donwgrade_percent=self.Down_per[0]
        self.M_Break_percenot= self.Break_percenot=self.break_Per[0]

        self.Fail_M_n = 0
        self.Break_M_n = 0
        self.Upgrade_M_n = 0
        self.Upgrade_M_list = [0]
        self.Break_M_list = [0]
        self.Fail_M_list = [0]

        # Graph Plot Init
        self.M_Fail = MpltCanvas()
        self.Upgrad_M_Graph()
        pass

    def Auto_Init_(self):
        self.A_Current_enforce = 0
        self.A_upgrade_percent = self.upgrade_percent=self.Up_Per[0]
        self.A_Donwgrade_percent = self.Donwgrade_percent=self.Down_per[0]
        self.A_Break_percenot= self.Break_percenot=self.break_Per[0]

        self.User=User()
        self.Upgrade_Try = 0
        self.Break_A_n = 0
        self.Fail_A_n = 0
        pass

    # 스타캐치 체크 시 효과 적용
    def StarCatch_Check(self, Current_enforce:int):
        if self.StarCatch_checkBox.isChecked() or self.StarCatch_checkBox_2.isChecked():
            upgrade_percent=self.Up_Per[Current_enforce]
            Donwgrade_percent=self.Down_per[Current_enforce]
            Break_percenot=self.break_Per[Current_enforce]
        else:
            upgrade_percent=self.St_Up_Per[Current_enforce]
            Donwgrade_percent=self.St_Down_per[Current_enforce]
            Break_percenot=self.st_break_Per[Current_enforce]

        return upgrade_percent, Donwgrade_percent, Break_percenot
    
    def Upgrade_Fail(self, Current_enforce:int, Break_n:int, User_Donwgrade_percent:int, User_Break_percenot:int, Mode:str='M'): 
        #강화 실패 시 확률
        Downgrade_percent = random.randrange(10001) 
        # print("Downgrade_percent:",Downgrade_percent/100,"%")

        # 파괴 + 하락확률 + 유지확률 = 100%
        User_Donwgrade_percent += User_Break_percenot

        # 현재 강화단계 저장
        Current_enforce_Save = Current_enforce
        Faril_break = Faril_down = False
        if Downgrade_percent <= User_Break_percenot: 
            # print("장비 파괴!")
            Faril_break = True
            Break_n += 1
            Current_enforce=12 #장비 전승
        elif Downgrade_percent <= User_Donwgrade_percent:
            Faril_down = True
            # print("강화 단계 하락 ↓\n")
            Current_enforce-=1 #강화단계 하락

        if Mode == 'M':
            # Mode = 'M': Manual = Defalt
            return Current_enforce, Break_n, Faril_break, Faril_down
        else : return Current_enforce, Break_n, Current_enforce_Save


####################################################################################################################################################
# Manual Tab
    # 스타캐치 체크 시 효과 적용: 수동
    def M_StarCatch_Check(self):
        self.M_upgrade_percent, self.M_Donwgrade_percent, self.M_Break_percenot = self.StarCatch_Check(self.M_Current_enforce)
        self.retranslateUi(Dialog)
        pass

    def Upgrade_Manual(self):
        # 창 사이즈 변경 Window resize
        Dialog.resize(447, 660)

        self.Upgrade_M_n+=1
        self.Upgrade_M_list.append(self.Upgrade_M_n)
        Upgrade_percent = random.randrange(10001)
        # print("현재 확률:",Upgrade_percent/100,"%")

        # 강화단계 확률 값 가져오기
        self.M_StarCatch_Check()
        if Upgrade_percent <= self.M_upgrade_percent:
            # print("강화 성공!")
            # print("강화 단계 상승 ↑")
            QtWidgets.QMessageBox.information(Dialog, "Succes", "장비 강화에 성공했습니다.")
            self.M_Current_enforce+=1
        else:
            # print("강화 실패!")
            self.Fail_M_n += 1
            self.M_Current_enforce, self.Break_M_n, Faril_break, Faril_down= self.Upgrade_Fail(self.M_Current_enforce, self.Break_M_n, self.M_Donwgrade_percent, self.M_Break_percenot)
            if Faril_break == True:
                QtWidgets.QMessageBox.warning(Dialog, "Fail", "장비 강화에 실패했습니다.\n 장비가 파괴되었습니다.")
            elif Faril_down == True: QtWidgets.QMessageBox.warning(Dialog, "Fail", "장비 강화에 실패했습니다.\n 강화단계가 하락합니다.")
            else : QtWidgets.QMessageBox.warning(Dialog, "Fail", "장비 강화에 실패했습니다.")
            
        
        self.M_Next_enforce=self.M_Current_enforce+1
        self.M_StarCatch_Check() # 다음 강화단계 각 확률 값 가져오기

        self.Break_M_list.append(self.Break_M_n)
        self.Fail_M_list.append(self.Fail_M_n)

        self.Upgrad_M_Graph()
        pass

    def Upgrad_M_Graph(self):
        self.M_Fail.axis.cla()
        self.M_Fail.axis.set_title("스타포스 강화 시뮬레이터")

        # print("Upgrad_list:", self.Upgrade_M_list)
        # print("Break_list:", self.Break_M_list)
        # print("Fail_list:", self.Fail_M_list)

        self.M_Fail.axis.set_xlabel("현재 강화 횟수:" + str(self.Upgrade_M_n))
        self.M_Fail.axis.plot(self.Upgrade_M_list , self.Fail_M_list, label="강화실패")
        self.M_Fail.axis.annotate("실패횟수:" + str(self.Fail_M_n), 
                                xy = (self.Upgrade_M_n*0.8, self.Fail_M_n*0.95))
        
        self.M_Fail.axis.plot(self.Upgrade_M_list , self.Break_M_list, label="장비파괴")
        self.M_Fail.axis.annotate("파괴횟수:" + str(self.Break_M_n), 
                                xy = (self.Upgrade_M_n*0.8, self.Break_M_n*2))
        
        if self.Fail_M_n!=0:
            self.M_Fail.axis.text( self.Upgrade_M_n*0.3, self.Fail_M_n*0.5, 
                                "실패율: {:.2f} %".format(self.Fail_M_n/self.Upgrade_M_n*100))
            
        self.M_Fail.axis.grid()
        self.M_Fail.axis.legend(loc = "upper left")
        self.M_Fail.draw()
        pass 



####################################################################################################################################################
# Auto Tab
    # 스타캐치 체크 시 효과 적용: 자동
    def A_StarCatch_Check(self):
        self.A_upgrade_percent, self.A_Donwgrade_percent, self.A_Break_percenot = self.StarCatch_Check(self.A_Current_enforce)
        pass

    def Auto_Upgrade_btn(self):
        # 창 사이즈 변경 Window resize:
        Dialog.resize(936, 976)
        
        # 그래프 초기화
        self.Upgrad_Auto_Graph_Init()
        print("\n자동강화 시뮬레이션 시작\n")

        self.User.Upgrade_Target_Value = self.User_Target_Value.currentText()
        self.User.Target_Goal_Times = self.User_Goal_Times.text()

        if self.User.Target_Goal_Times.isdecimal():
            # 목표 단계
            self.User.Upgrade_Target_Value = int(self.User.Upgrade_Target_Value)
            # 목표 완성 횟수
            self.User.Target_Goal_Times = int(self.User.Target_Goal_Times)
            self.Uprade_Auto()
        else: 
            QtWidgets.QMessageBox.information(Dialog, "알림", "'목표도달 횟수'는 정수로만 입력해주세요.")
        self.Auto_Init_()
        pass

    def Auto_Dict_Init(self):
        # 각 단계 별 실패횟수 누적, 장비가 바뀔 때 초기화
        self.Fail_Auto_Dict = {}
        # 각 단계 별 파괴횟수 누적, 장비가 바뀔 때 초기화
        self.Break_Auto_Dict = {}
        pass

    def Uprade_Auto(self):
        self.User.Upgrade_Target_Value
        self.User.Target_Goal_Times

        equipment = "0성->"+str(self.User.Upgrade_Target_Value)+"성 장비 별 강화시도 횟수"
        All_Try = {equipment: []}
        Cumul_Fail_dict = {}
        Cumul_Break_dict = {}

        QtWidgets.QMessageBox.information(Dialog, "알림", "자동 강화를 시작합니다. \n화면을 건들지 마십시오.")
        while self.Upgrade_Try < self.User.Target_Goal_Times:
            self.Upgrade_Try += 1
            Upgrade_A_n = 0
            Try = 0

            self.Auto_Dict_Init()
            print(str(self.Upgrade_Try)+"번 째 장비 강화시도")
            while Upgrade_A_n < self.User.Upgrade_Target_Value:
                self.Fail_A_n = 0
                self.Break_A_n = 0
                self.A_Current_enforce = Upgrade_A_n
                
                # 딕셔너리 키의 강화단계가 없을 경우 동적 생성
                if Upgrade_A_n not in self.Fail_Auto_Dict.keys():
                    # print(Upgrade_A_n not in self.Fail_Auto_Dict.keys())
                    self.Fail_Auto_Dict[Upgrade_A_n] = 0
                if Upgrade_A_n not in self.Break_Auto_Dict.keys():
                    # print(Upgrade_A_n not in self.Break_Auto_Dict.keys())
                    self.Break_Auto_Dict[Upgrade_A_n] = 0
                
                self.A_StarCatch_Check() # 강화단계 각 확률 가져오기
                Upgrade_percent = random.randrange(10001) #확률 값 뽑기
                # print("Upgrade_A_n:", Upgrade_A_n)
                # print("self.A_upgrade_percent:", self.A_upgrade_percent/100, '%')
                # print("self.Upgrade_percent:", Upgrade_percent/100, '%\n')

                # 성공 확률 비교
                if Upgrade_percent <= self.A_upgrade_percent:
                    Upgrade_A_n += 1
                else: #실패 시
                    # 실패 횟수 증가
                    self.Fail_A_n = 1

                    # print("self.A_Donwgrade_percent:", self.A_Donwgrade_percent/100, '%')
                    # print("self.A_Break_percenot:", self.A_Break_percenot/100, '%\n')
                    Upgrade_A_n, self.Break_A_n, Upgrade_A_b = self.Upgrade_Fail(Upgrade_A_n, self.Break_A_n, self.A_Donwgrade_percent, self.A_Break_percenot, 'a')
                    # 딕셔너리의 값 추가
                    self.Fail_Auto_Dict[Upgrade_A_b] += self.Fail_A_n
                    self.Break_Auto_Dict[Upgrade_A_b] += self.Break_A_n
                    pass
                # 강화 시도 횟수 누적
                Try += 1
                # print(f"Try: {Try}\n")
                pass
            All_Try[equipment].append(Try)
            Cumul_Fail_dict["장비"+str(self.Upgrade_Try)] = self.Fail_Auto_Dict
            Cumul_Break_dict["장비"+str(self.Upgrade_Try)] = self.Break_Auto_Dict

            {# print("Goal_Times:",self.Upgrade_Try)

            # print("Fail ", self.Fail_Auto_Dict.keys())
            # print("Fail ", self.Fail_Auto_Dict.values())
            # print("Fail_", self.Fail_Auto_Dict.items())
            # print("Fail_Auto_Dict len:", len(self.Fail_Auto_Dict))
                
            # print("Break ", self.Break_Auto_Dict.keys())
            # print("Break ", self.Break_Auto_Dict.values())
            # print("Break ", self.Break_Auto_Dict.items())
            # print("Break_Auto_Dict len:", len(self.Break_Auto_Dict))
            # print()
            }

            self.Upgrad_A_Fail_Graph(self.Fail_Auto_Dict.values(), len(self.Fail_Auto_Dict), "장비"+str(self.Upgrade_Try)+" 누적 실패")
            self.Upgrad_A_Break_Graph(self.Break_Auto_Dict.values(), len(self.Break_Auto_Dict), "장비"+str(self.Upgrade_Try)+" 누적 파괴")
            pass
        # DataFrame 생성
        Try_DF, Cumul_Fail_DF, Cumul_Break_DF = self.Create_DataFrame(All_Try, Cumul_Fail_dict, Cumul_Break_dict, equipment)
        Fail_Stats_DF, Break_Stats_DF = self.Create_DataFrame_Stats(Cumul_Fail_DF, Cumul_Break_DF)

        #엑셀 파일에 여러 개 시트로 생성
        self.Create_ExcelFile(Try_DF, Cumul_Fail_DF, Cumul_Break_DF, Fail_Stats_DF, Break_Stats_DF)
        print("\n자동강화 완료 시뮬레이션 종료")
        QtWidgets.QMessageBox.information(Dialog, "시뮬레이션 자동강화 완료", "시뮬레이션 자동강화가 완료되었습니다.")
        pass

    # Auto Graph
    def Upgrad_Auto_Graph_Init(self):
        # 그래프 초기화
        self.Auto_Fail_Graph.axis.cla()
        self.Auto_Fail_stats_Graph.axis.cla()
        self.Auto_Break_Graph.axis.cla()
        self.Auto_Break_stats_Graph.axis.cla()
        # 그래프 딕셔너리 초기화
        self.Auto_Dict_Init()
        pass

    def Upgrad_A_Fail_Graph(self, Dict_Value:list, Dict_len:int, Graph_Label:str):
        '''
        Auto_Fail_axis = class,
        ylim = np.array(len)
        '''
        self.Auto_Fail_Graph.axis.set_title("스타포스 자동 강화 시뮬레이터")
        Xplot = np.arange(Dict_len)
        if self.Upgrade_Try < 6: self.line, = self.Auto_Fail_Graph.axis.plot(Xplot, Dict_Value, label = Graph_Label)
        elif self.Upgrade_Try == 6: self.line, = self.Auto_Fail_Graph.axis.plot(Xplot, Dict_Value, label = "  . . . ")
        else: self.line, = self.Auto_Fail_Graph.axis.plot(Xplot, Dict_Value)
        self.Auto_Fail_Graph.axis.grid()
        self.Auto_Fail_Graph.axis.legend(loc = "upper left")
        self.Auto_Fail_Graph.draw()
        pass

    def Upgrad_A_Break_Graph(self, Dict_Value:list, Dict_len:int, Graph_Label:str):
        '''
        Auto_Break_axis = class,
        ylim = np.array(len)
        '''
        Yplot = np.arange(Dict_len)
        if self.Upgrade_Try < 6: self.Auto_Break_Graph.axis.plot(Yplot, Dict_Value, label = Graph_Label)
        elif self.Upgrade_Try == 6: self.Auto_Break_Graph.axis.plot(Yplot, Dict_Value, label = "  . . . ")
        else: self.Auto_Break_Graph.axis.plot(Yplot, Dict_Value)
        self.Auto_Break_Graph.axis.grid()   
        self.Auto_Break_Graph.axis.legend(loc = "upper left")
        self.Auto_Break_Graph.draw()
        pass

    def Upgrad_A_Fail_stats_Graph(self, Dict_Value:list, Dict_len:int, Graph_Label:str):
        '''
        Auto_Fail_stats_axis = class,
        ylim = np.array(len)
        '''
        # self.Auto_Fail_stats_Graph.axes.set_title("스타포스 자동 강화 시뮬레이터")
        Yplot = np.arange(Dict_len)
        self.Auto_Fail_stats_Graph.axis.plot(Yplot, Dict_Value, label = Graph_Label)
        self.Auto_Fail_stats_Graph.axis.grid()   
        self.Auto_Fail_stats_Graph.axis.legend(loc = "upper left")
        self.Auto_Fail_stats_Graph.draw()
        pass

    def Upgrad_A_Break_stats_Graph(self, Dict_Value:list, Dict_len:int, Graph_Label:str):
        '''
        Auto_Fail_ax = class,
        ylim = np.array(len)
        '''
        Yplot = np.arange(Dict_len)
        self.Auto_Break_stats_Graph.axis.plot(Yplot, Dict_Value, label = Graph_Label)
        self.Auto_Break_stats_Graph.axis.grid()   
        self.Auto_Break_stats_Graph.axis.legend(loc = "upper left")
        self.Auto_Break_stats_Graph.draw()
        pass

    # Auto DataFrame
    def Create_DataFrame(self, All_Try:dict, Fail_Cumul_dict:dict, Break_Cumul_dict:dict, equipment):
        # 강화 시도 횟수
        equi_IDX = ["장비"+str(i) for i in np.arange(1,self.Upgrade_Try+1)]
        Try_DF = pd.DataFrame(All_Try, index=equi_IDX)
        equi_IDX.append("평균 강화시도 횟수")
        # 평균 강화시도 횟수
        All_Try[equipment].append(float(Try_DF.mean(axis="index").iloc[0])) 
        # float(Try_DF.mean(axis="index", numeric_only = True))
        Try_DF = pd.DataFrame(All_Try, index=equi_IDX)

        # 누적 실패량 데이터프레임
        Try_Fail_DF = pd.DataFrame(Fail_Cumul_dict)
        # 누적 파괴량 데이터프레임
        Try_Break_DF = pd.DataFrame(Break_Cumul_dict)

        {# print("DataFrame")
        # display(Try_DF)
        # display(Try_Fail_DF)
        # display(Try_Break_DF)
        }
        return Try_DF, Try_Fail_DF, Try_Break_DF
    
    def Create_DataFrame_Stats(self, Stats_Fail_DF:pd.DataFrame, Stats_Break_DF:pd.DataFrame):
        Label_list = ["최대", "평균", "최소"]

        # 평균 누적 실패량
        Fail_Stats_dict = {}
        Graph_Label = " 누적 실패량"
        Fail_Stats_dict[Label_list[0]+Graph_Label] = Stats_Fail_DF.max(axis="columns")
        Fail_Stats_dict[Label_list[1]+Graph_Label] = Stats_Fail_DF.mean(axis="columns")
        Fail_Stats_dict[Label_list[2]+Graph_Label] = Stats_Fail_DF.min(axis="columns")
        for label_str in Label_list:
            self.Upgrad_A_Fail_stats_Graph(list(Fail_Stats_dict[label_str+Graph_Label]), len(self.Fail_Auto_Dict),
            label_str+Graph_Label)
        Stats_Fail_DF = pd.DataFrame(Fail_Stats_dict)

        # 평균 누적 실패량
        Break_Stats_dict = {}
        Graph_Label = " 누적 파괴량"
        Break_Stats_dict[Label_list[0]+Graph_Label] = Stats_Break_DF.max(axis="columns")
        Break_Stats_dict[Label_list[1]+Graph_Label] = Stats_Break_DF.mean(axis="columns")
        Break_Stats_dict[Label_list[2]+Graph_Label] = Stats_Break_DF.min(axis="columns")
        for label_str in Label_list:
            self.Upgrad_A_Break_stats_Graph(list(Break_Stats_dict[label_str+Graph_Label]), len(self.Break_Auto_Dict),
            label_str+Graph_Label)
        Stats_Break_DF = pd.DataFrame(Break_Stats_dict)
        return Stats_Fail_DF, Stats_Fail_DF

    #엑셀 파일에 여러 개 시트로 생성
    def Create_ExcelFile(self, Try_DF:pd.DataFrame, Fail_Cumul_DF:pd.DataFrame, Break_Cumul_DF:pd.DataFrame, Fail_Stats_DF:pd.DataFrame, Break_Stats_DF:pd.DataFrame):
        if self.StarCatch_checkBox_2.isChecked():
            isChecked = "(스타포스 체크해제)"
        else: isChecked = "(스타포스 체크)"

        #0. 폴더 생성
        self.CreateFolder("시뮬레이션 결과")
        #1. 파일 생성
        writer=pd.ExcelWriter("./시뮬레이션 결과/"+str(self.User.Upgrade_Target_Value)+"강 강화"+str(self.User.Target_Goal_Times)+"개 장비 시뮬레이션 결과"+isChecked+".xlsx")
        #2. 생성 파일에 시트명 지정 후 dataframe에 저장한 결과값 넣기
        Try_DF.to_excel(writer, sheet_name='총 강화시도 횟수')
        Fail_Cumul_DF = Fail_Cumul_DF.transpose() # 행, 열 바꾸기
        Fail_Cumul_DF.to_excel(writer, sheet_name='각 장비 별 누적 실패량')
        Break_Cumul_DF = Break_Cumul_DF.transpose() # 행, 열 바꾸기
        Break_Cumul_DF.to_excel(writer, sheet_name='각 장비 별 누적 파괴량')
        Fail_Stats_DF.to_excel(writer, sheet_name='평균 누적 실패량')
        Break_Stats_DF.to_excel(writer, sheet_name='평균 누적 파괴량')
        writer.close() # 파일 닫기
        pass

    def CreateFolder(self, directory:str):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)


####################################################################################################################################################
# rediction Tab
    def Upgrade_prediction(self):
        pass
    

####################################################################################################################################################
# UI 레이아웃, 위젯 설정 / Layout, Widget Setting
    def setupUi(self, Dialog):
        Dialog.setObjectName("메이플 스타포스 강화 Simulator")
        Dialog.resize(936, 976)
        Dialog.setMinimumSize(QtCore.QSize(447, 660))
        Dialog.setMaximumSize(QtCore.QSize(936, 976))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog.setWhatsThis("")
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(3, 0, 935, 975))
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab_Manual()
        self.tab_Auto()
        self.tab_parediction()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        pass
    

    # Tab
    def tab_Manual(self):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.Main_Base_img = QtWidgets.QLabel(self.tab)
        self.Main_Base_img.setGeometry(QtCore.QRect(0, 0, 361, 261))
        self.Main_Base_img.setStyleSheet("image: url(:/image/스타포스.jpg);")
        self.Main_Base_img.setObjectName("label_5")

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Text = QtWidgets.QLabel(self.tab)
        self.Title_Text.setFont(font)
        self.Title_Text.setGeometry(QtCore.QRect(41, 20, 277, 41))
        self.Title_Text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title_Text.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.489227, y2:0, stop:0 rgba(0, 27, 126, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.489227, y2:0, stop:0.113636 rgba(0, 71, 166, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Title_Text.setTextFormat(QtCore.Qt.AutoText)
        self.Title_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_Text.setWordWrap(False)
        self.Title_Text.setObjectName("label")

        self.Succes_Persent_Text = QtWidgets.QLabel(self.tab)
        self.Succes_Persent_Text.setGeometry(QtCore.QRect(134, 106, 97, 16))
        self.Succes_Persent_Text.setStyleSheet("image: url(:/image/성공확률Text.jpg);")
        self.Succes_Persent_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Succes_Persent_Text.setObjectName("label_2")

        self.Down_percent_Text = QtWidgets.QLabel(self.tab)
        self.Down_percent_Text.setGeometry(QtCore.QRect(147, 118, 116, 32))
        self.Down_percent_Text.setStyleSheet("image: url(:/image/실패(하락)확률Text.jpg);")
        self.Down_percent_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Down_percent_Text.setObjectName("label_3")

        self.Destruction_percent_Text = QtWidgets.QLabel(self.tab)
        self.Destruction_percent_Text.setGeometry(QtCore.QRect(136, 146, 97, 16))
        self.Destruction_percent_Text.setStyleSheet("image: url(:/image/파괴확률Text.jpg);")
        self.Destruction_percent_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Destruction_percent_Text.setObjectName("label_4")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.Current_enforce_Text = QtWidgets.QLabel(self.tab)
        self.Current_enforce_Text.setGeometry(QtCore.QRect(150, 80, 71, 26))
        self.Current_enforce_Text.setFont(font)
        self.Current_enforce_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.Current_enforce_Text.setObjectName("label_9")

        self.Next_enforce_Text = QtWidgets.QLabel(self.tab)
        self.Next_enforce_Text.setGeometry(QtCore.QRect(211, 80, 71, 26))
        self.Next_enforce_Text.setFont(font)
        self.Next_enforce_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.Next_enforce_Text.setObjectName("label_11")

        self.Succese_percent_Val_Text = QtWidgets.QLabel(self.tab)
        self.Succese_percent_Val_Text.setGeometry(QtCore.QRect(220, 99, 71, 26))
        self.Succese_percent_Val_Text.setFont(font)
        self.Succese_percent_Val_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.Succese_percent_Val_Text.setObjectName("label_6")

        self.Down_percent_val_Text = QtWidgets.QLabel(self.tab)
        self.Down_percent_val_Text.setGeometry(QtCore.QRect(267, 119, 71, 26))
        self.Down_percent_val_Text.setFont(font)
        self.Down_percent_val_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.Down_percent_val_Text.setObjectName("label_7")

        self.Destruction_percent_Val_Text = QtWidgets.QLabel(self.tab)
        self.Destruction_percent_Val_Text.setGeometry(QtCore.QRect(224, 140, 71, 26))
        self.Destruction_percent_Val_Text.setFont(font)
        self.Destruction_percent_Val_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.Destruction_percent_Val_Text.setObjectName("label_8")

        self.StarCatch_checkBox = QtWidgets.QCheckBox(self.tab)
        self.StarCatch_checkBox.setGeometry(QtCore.QRect(156, 190, 191, 52))
        self.StarCatch_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StarCatch_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.StarCatch_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StarCatch_checkBox.clicked.connect(self.M_StarCatch_Check)
        self.StarCatch_checkBox.setStyleSheet("image: url(:/image/스타캐치 해제 체크.jpg);")
        self.StarCatch_checkBox.setCheckable(True)
        self.StarCatch_checkBox.setObjectName("checkBox")

        self.enforce_Button = QtWidgets.QPushButton(self.tab)
        self.enforce_Button.setGeometry(QtCore.QRect(18, 197, 128, 37))
        self.enforce_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enforce_Button.clicked.connect(self.Upgrade_Manual)
        self.enforce_Button.setStyleSheet("image: url(:/image/강화버튼.jpg);")
        self.enforce_Button.setObjectName("pushButton")

        # Graph Canvas
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-25, 260, 500, 370))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graph_verticalLayout.setObjectName("verticalLayout")
        self.graph_verticalLayout.addWidget(self.M_Fail)

        self.Main_Base_img.raise_()
        self.Title_Text.raise_()
        self.Current_enforce_Text.raise_()
        self.Next_enforce_Text.raise_()
        self.Destruction_percent_Text.raise_()
        self.Succes_Persent_Text.raise_()
        self.Down_percent_Text.raise_()
        self.Succese_percent_Val_Text.raise_()
        self.Down_percent_val_Text.raise_()
        self.Destruction_percent_Val_Text.raise_()
        self.enforce_Button.raise_()
        self.StarCatch_checkBox.raise_()
        self.verticalLayoutWidget.raise_()
        pass

    def tab_Auto(self):
        self.tab_Upgrade_A = QtWidgets.QWidget()
        self.tab_Upgrade_A.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_Upgrade_A, "")

        self.Main_Base_img_2 = QtWidgets.QLabel(self.tab_Upgrade_A)
        self.Main_Base_img_2.setGeometry(QtCore.QRect(0, 0, 361, 261))
        self.Main_Base_img_2.setStyleSheet("image: url(:/image/스타포스.jpg);")
        self.Main_Base_img_2.setObjectName("label_12")

        self.StarCatch_checkBox_2 = QtWidgets.QCheckBox(self.tab_Upgrade_A)
        self.StarCatch_checkBox_2.setGeometry(QtCore.QRect(156, 190, 191, 52))
        self.StarCatch_checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StarCatch_checkBox_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.StarCatch_checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StarCatch_checkBox_2.setStyleSheet("image: url(:/image/스타캐치 해제 체크.jpg);")
        self.StarCatch_checkBox_2.setCheckable(True)
        self.StarCatch_checkBox_2.setObjectName("checkBox_2")
        
        self.Title_label_2 = QtWidgets.QLabel(self.tab_Upgrade_A)
        self.Title_label_2.setGeometry(QtCore.QRect(28, 20, 305, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Title_label_2.setFont(font)
        self.Title_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title_label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.489227, y2:0, stop:0 rgba(0, 27, 126, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.489227, y2:0, stop:0.113636 rgba(0, 71, 166, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Title_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.Title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label_2.setWordWrap(False)
        self.Title_label_2.setObjectName("label_13")

        self.pushButton_2 = QtWidgets.QPushButton(self.tab_Upgrade_A)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 197, 128, 37))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.clicked.connect(self.Auto_Upgrade_btn)
        self.pushButton_2.setStyleSheet("image: url(:/image/강화버튼.jpg);")
        self.pushButton_2.setObjectName("pushButton_2")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.Target_label = QtWidgets.QLabel(self.tab_Upgrade_A)
        self.Target_label.setEnabled(True)
        self.Target_label.setFont(font)
        self.Target_label.setGeometry(QtCore.QRect(144, 70, 191, 51))
        self.Target_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Target_label.setObjectName("label_17")
        
        self.Times_label = QtWidgets.QLabel(self.tab_Upgrade_A)
        self.Times_label.setFont(font)
        self.Times_label.setGeometry(QtCore.QRect(144, 70+51, 191, 51))
        self.Times_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Times_label.setObjectName("label_16")

        self.User_Target_Value = QtWidgets.QComboBox(self.tab_Upgrade_A)
        self.User_Target_Value.setGeometry(QtCore.QRect(144+120, 85, 60, 20))
        for i in range(25):
            self.User_Target_Value.addItem(str(i+1))
        self.User_Target_Value.setObjectName("comboBox")

        self.User_Goal_Times = QtWidgets.QLineEdit(self.tab_Upgrade_A)
        self.User_Goal_Times.setGeometry(QtCore.QRect(144+120, 85+50, 60, 20))
        self.User_Goal_Times.setObjectName("lineEdit_2")

        # Graph Layout Canvas
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_Upgrade_A)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(-5, 590, 500, 370))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.graph_verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.graph_verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.graph_verticalLayout_3.setObjectName("verticalLayout_9")
        self.graph_verticalLayout_3.addWidget(self.Auto_Break_Graph)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_Upgrade_A)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-5, 260, 500, 370))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.graph_verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.graph_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graph_verticalLayout_2.setObjectName("verticalLayout_4")
        self.graph_verticalLayout_2.addWidget(self.Auto_Fail_Graph)

        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_Upgrade_A)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(450, 590, 500, 370))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.graph_verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.graph_verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.graph_verticalLayout_5.setObjectName("verticalLayout_11")
        self.graph_verticalLayout_5.addWidget(self.Auto_Break_stats_Graph)

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_Upgrade_A)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(450, 260, 500, 370))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.graph_verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.graph_verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.graph_verticalLayout_4.setObjectName("verticalLayout_10")
        self.graph_verticalLayout_4.addWidget(self.Auto_Fail_stats_Graph)

        self.Main_Base_img_2.raise_()
        self.StarCatch_checkBox_2.raise_()
        self.Title_label_2.raise_()
        self.pushButton_2.raise_()
        self.Target_label.raise_()
        self.Times_label.raise_()
        self.User_Target_Value.raise_()
        self.User_Goal_Times.raise_()
        pass
    
    def tab_parediction(self):
        self.tab_prediction = QtWidgets.QWidget()
        self.tab_prediction.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_prediction, "")

        pass

####################################################################################################################################################
# UI 값 표시 Value View
    def retranslateUi(self, Dialog):
        self.Upgrad_M_Graph
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "메이플스토리 스타포스 강화 Simulator"))

        self.Manua_Tab_Value_View(_translate)
        self.Auto_Tab_Value_View(_translate)
        self.prediction_Tab_Value_View(_translate)
        pass

    def Manua_Tab_Value_View(self, _translate):
        self.Title_Text.setText(_translate("Dialog", "메이플 스타포스 강화"))
        #현재 강화
        self.Current_enforce_Text.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Current_enforce_Text.setText(_translate("Dialog", str(self.M_Current_enforce)+" 성  >"))
        #다음 강화
        self.Next_enforce_Text.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Next_enforce_Text.setText(_translate("Dialog", str(self.M_Next_enforce)+" 성"))
        #강화 성공 확률
        self.Succese_percent_Val_Text.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Succese_percent_Val_Text.setText(_translate("Dialog", str(self.M_upgrade_percent/100)+" %"))
        #실패 시 하락 확률 
        self.Down_percent_val_Text.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Down_percent_val_Text.setText(_translate("Dialog", str(self.M_Donwgrade_percent/100)+" %"))
        #실패 시 파괴 확률
        self.Destruction_percent_Val_Text.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Destruction_percent_Val_Text.setText(_translate("Dialog", str(self.M_Break_percenot/100)+" %"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "수동"))
        pass
    
    def Auto_Tab_Value_View(self, _translate):
        self.Title_label_2.setText(_translate("Dialog", "메이플 스타포스 자동강화"))
        self.Target_label.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Target_label.setText(_translate("Dialog", "강화 목표"))
        self.Times_label.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">vasfsf</span></p></body></html>"))
        self.Times_label.setText(_translate("Dialog", "강화장비 갯수"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Upgrade_A), _translate("Dialog", "자동"))
        pass

    def prediction_Tab_Value_View(self, _translate):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prediction), _translate("Dialog", "예측"))

        pass   
    
    pass


{# def Upgrad_Graph():
#     plt.cla()
#     plt.rc('font', family='Malgun Gothic')
#     plt.title("스타포스 강화 시뮬레이터")

#     print("Upgrad_list:", Upgrad_list)
#     print("Break_list:", Break_list)
#     print("Fail_list:", Fail_list)

#     plt.xlabel("현재 강화 횟수:" + str(Upgrad_n))

#     plt.plot(Upgrad_list , Fail_list, label="강화실패")
#     plt.annotate("실패횟수:" + str(Fail_n), xy = \
#                 (Upgrad_n, Fail_n))
    
#     plt.plot(Upgrad_list , Break_list, label="장비파괴")
#     plt.annotate("파괴횟수:" + str(Break_n), xy = \
#                 (Upgrad_n, Break_n))
    
#     if Fail_n!=0:
#         plt.text( Upgrad_n*0.3, Fail_n*0.5, "실패율: {:.2f} %".format(Fail_n/Upgrad_n*100))
        
#     plt.legend(loc = "upper left")
#     # plt.pause(1/10000)
#     pass
}

{#계단 그래프
# ax.step(Upgrad_list, Fail_list, linewidth=1)

# ax.set(xlim=(0, len(Upgrad_list)), xticks=np.arange(1, len(Upgrad_list)),
#         ylim=(0, len(Fail_list)), yticks=np.arange(1, len(Fail_list)))
}

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())