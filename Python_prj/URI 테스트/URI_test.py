import requests
from bs4 import BeautifulSoup

URi = "http://localhost:8080/api/v1/get-api/request2?name=name&email=email@mail.com&organization=think-ground"

URi = "http://localhost:8080/greed"

response  = requests.get(URi)
response .raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
body = soup.find("body")

print(soup)
    
# 이 PageElement의 하위 항목을 살펴보고 지정된 기준과 일치하는 첫 번째 PageElement를 찾습니다.
# 모든 find_* 메소드는 공통 인수 세트를 사용합니다. 자세한 설명은 온라인 설명서를 참조하세요.

# :param name: 태그 이름에 대한 필터입니다.
# :param attrs: 속성 값에 대한 필터 사전입니다.
# :param recursive: 이것이 True이면 find()는 다음을 수행합니다. 
#     이 PageElement의 하위 항목을 재귀적으로 검색합니다. 그렇지 않으면 직계 자식만 고려됩니다.
# :param limit: 이렇게 많은 결과를 찾은 후에는 검색을 중지하세요.
# :kwargs: 속성 값에 대한 필터 사전입니다.
# :return: PageElement.
# :rtype: bs4.element.Tag | bs4.element.NavigableString