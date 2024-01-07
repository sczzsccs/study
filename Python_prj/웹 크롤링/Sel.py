# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 크롬 드라이버 자동 업데이트 및 꺼짐방지
driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("http://naver.com")

#검색 창 입력 및 검색버튼 클릭
driver.find_element(By.CLASS_NAME, "search_input").send_keys("Google지도")
driver.find_element(By.ID, "search-btn").click()
print("Google 지도 검색 완료")
driver.find_element(By.CLASS_NAME, "link_tit").click()
print("Google 지도 이동 완료")

#네이버지도 검색
time.sleep(3)
driver.switch_to.window(driver.window_handles[0]) #첫번째 탭으로 이동
driver.find_element(By.ID, "nx_query").clear()
driver.find_element(By.ID, "nx_query").send_keys("네이버지도")
driver.find_element(By.CLASS_NAME, "bt_search").click()
print("네이버 지도 검색 완료")
driver.find_element(By.CLASS_NAME, "link_name").click()
print("네이버 지도 이동 완료")

#맛 집 검색
time.sleep(3)
driver.switch_to.window(driver.window_handles[0]) #첫번째 탭으로 이동
driver.find_element(By.ID, "nx_query").clear()
driver.find_element(By.ID, "nx_query").send_keys("맛 집")
driver.find_element(By.CLASS_NAME, "bt_search").click()
print("맛 집 검색 완료")
#이미지 클릭
driver.find_element(By.LINK_TEXT, "이미지").click()
#로딩 대기시간
time.sleep(2)
print("맛 집 이미지 로드 완료")
#이미지 탐색
for i in range(15):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    if i%3==0:
        print("이미지 로딩 중...")
        time.sleep(0.7)
        print("이미지 로드 완료")
    time.sleep(0.5)
#탐색 종료 알림
print("맛 집 탐색 종료")


{# 불필요한 에러 메시지 삭제
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
# service = Service(executable_path=ChromeDriverManager().install())
}