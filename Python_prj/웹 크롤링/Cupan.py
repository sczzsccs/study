import requests
import re
from bs4 import BeautifulSoup

head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

for i in range(1,6):
    url="https://www.coupang.com/np/search?q=%ED%83%9C%EB%B8%94%EB%A6%BF&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)

    res=requests.get(url, headers=head)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")

    items=soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        #광고 상품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print(" <광고 상품 제외>")
            continue
        
        #상품명
        name = item.find("div", attrs={"class":"name"}).ge_text()

        #애플상품 제외
        if "Apple" in name:
            print(" <애플 상품 제외>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).ge_text()

        #리뷰 100개 이상, 평점 4.5 이상만 조회
        #펑점
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate=rate.get_text()
            #리뷰 수
            rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()
            rate_cnt = rate_cnt[1:-1]
            if float(rate_cnt) >= 4.5 and rate >=100:
                print(
                    "상품명:", name,
                    "\nprice:", price,
                    "\n평점:", rate,
                    "\n리뷰 개수:", rate_cnt)
        else:
            print(" <리뷰없는 상품 제외>")
            continue
        print()