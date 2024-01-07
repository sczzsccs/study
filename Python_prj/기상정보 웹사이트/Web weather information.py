from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from flask import Flask

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://weather.naver.com/typhoon/02390102")
soup = bs(driver.page_source, "html.parser")
driver.implicitly_wait(10)

#Flask 객체 인스턴스 생성
app = Flask(__name__)

text = str(soup)
with open('네이버 태풍정보.html', 'w', encoding='UTF8') as html_file:
    html_file.write(text)
    html_file.close()

driver.get("https://weather.naver.com/typhoon/02390102")
soup = bs(driver.page_source, "html.parser")
html_text = ""

# 태풍정보
ul = soup.select_one("#content > div.section_wrap > div.section_center > div:nth-child(10) > div")
titles = ul.select("div.report > p")
for text in titles:
    html_text+=(str(text))

# #news
ul = soup.select_one("#news > ul")
titles = ul.select('li > a')
for text in titles:
    html_text+=(str(text))

# print(html_text)
with open('태풍정보.html', 'w', encoding='UTF8') as html_file:
    html_file.write(str(html_text))
    html_file.close()

@app.route('/') # 접속하는 url
def index():
    return html_text

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)