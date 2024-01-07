# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

import time
import tkinter as TK
import tkinter.ttk as ttk
import tkinter.font as tf
import tkinter.messagebox as tm
window=TK.Tk()

window.title("웹 크롤링")
window.geometry("420x270+500+150")
font=tf.Font(size=15, weight="bold")
font2=tf.Font(size=12, weight="normal")

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

print("-------자동검색을 시작합니다-------")
time.sleep(0.3)
print("---------크롬을 실행합니다---------")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
time.sleep(0.3)
print("---크롬이 성공적으로 실행됐습니다.---")
#시작 웹 페이지
web="http://google.com"
driver.get(web)
Scroll=15
Tab_n=2

print("----검색할 키워드를 입력해주세요.----\n")

def Search():
    Keword=Kward_Ent.get()

    global web
    web=Site_Ent.get()
    if not web:
        web="http://google.com"
    driver.get(web)

    global Scroll
    if Scroll_Ent.get()[-1] == "회":
        Scroll=int(Scroll_Ent.get()[:-2])
    else:
        Scroll=int(Scroll_Ent.get())
        Scroll_Ent.delete(0, "end")
        Scroll_Ent.insert("end", str(Scroll)+" 회")   

    web_title=driver.find_element(By.TAG_NAME, "title").get_attribute("innerText")

    print("-현재 사이트:", web_title, "-----")
    print("입력된 키워드:", Keword)

    if "Google" == web_title:
        driver.find_element(By.ID, "APjFqb").send_keys(Keword)
        driver.find_element(By.ID, "APjFqb").send_keys(Keys.ENTER)
    elif "NAVER" == web_title:
        driver.find_element(By.ID, "query").send_keys(Keword)
        driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
    elif "Daum" == web_title:
        driver.find_element(By.CLASS_NAME, "tf_keyword").send_keys(Keword)
        driver.find_element(By.CLASS_NAME, "tf_keyword").send_keys(Keys.ENTER)

    else:
        tm.showerror("erroe!", "현재 주소 창에서는\n탐색이 불가능합니다!\n주소를 바꿔서 다시 시도하세요.")
        tm.showinfo("알림", "다음의 사이트 주소에서만 탐색이 가능합니다.\n'Google.com', 'Naver.com', 'Daum.net'")
        print("Error!: 현재 사이트에서는 탐색이 불가능 합니다! \n사이트 주소를 바꿔주세요!")
        return
    print("-----키워드 검색 완료-----\n")

    if web_title == "Daum":
        driver.find_element(By.LINK_TEXT, "더보기/접기").click()

    driver.find_element(By.LINK_TEXT, "이미지").click()
    print("-이미지 검색을 시작합니다.-\n")

    #이미지 탐색
    for i in range(Scroll):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        if i%3==0:
            print("이미지 로딩 중...")
            time.sleep(0.7)
            print("이미지 로드 완료")
        time.sleep(0.5)
    #탐색 종료 알림
    print("-------------검색 완료-------------\n\n")
    tm.showinfo("알림", "탐색이 완료 되었습니다.\n새로운 키워드를 입력하시면 새 탐색이 시작됩니다.")

    time.sleep(0.2)
    print("----검색할 키워드를 입력해주세요.----")
    return

Label_Title=TK.Label(window, text="웹 크롤링", font=font)
Label_Title.place(x=170, y=15)

Kward_Label=TK.Label(window, text="Kward", font=font2).place(x=80, y=68)
Kward_Ent=TK.Entry(window, width=20, font=font2)
Kward_Ent.place(x=135, y=68)
Kward_Btn=TK.Button(window, padx=5, text="검색", command=Search, font=font2).place(x=310, y=63)

Scroll_Title=TK.Label(window, text="Scroll", font=font2)
Scroll_Title.place(x=50, y=105)

Scroll_Ent=TK.Entry(window, width=5, font=font2, justify="center")
Scroll_Ent.insert(0, str(Scroll)+" 회")
Scroll_Ent.place(x=100, y=105)

def New_Tab():
    global Tab_n
    Tab_n+=1
    global web
    web=Site_Ent.get()
    if not web:
        web="http://google.com"
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(web)
    Tab_Val=[str(i) + " 탭" for i in range(1, Tab_n)]
    Tab_com_box['values']=Tab_Val
    return

def Move_Tab():
    Tab=int(Tab_com_box.get()[:-1])-1
    driver.switch_to.window(driver.window_handles[Tab])
    return

combo_Val=[str(i) + " 탭" for i in range(1, Tab_n)]
Tab_com_box=ttk.Combobox(window, width=10, height=5, values=combo_Val, justify="center", state="readonly")
Tab_com_box.current(0)
Tab_com_box.place(x=175, y=105)

Move_Tab_Btn=TK.Button(window, padx=3, text="탭 이동", command=Move_Tab).place(x=150, y=135)
New_Tab_Btn=TK.Button(window, padx=3, text="새 탭 이동", command=New_Tab).place(x=225, y=135)

def Site_Move():
    global web
    web=Site_Ent.get()
    if not web:
        web="http://google.com"
    driver.get(web)
    return

Site_Label=TK.Label(window, text="Site 주소", font=font2).place(x=55, y=183)
Site_Ent=TK.Entry(window, width=30, font=font2, justify="center")
Site_Ent.insert(0, web)
Site_Ent.place(x=135, y=183)
Site_Btn=TK.Button(window, text="사이트 이동", command=Site_Move, font=font2).place(x=170, y=215)

window.mainloop()