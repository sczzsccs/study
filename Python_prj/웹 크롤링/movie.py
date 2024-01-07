import requests
from bs4 import BeautifulSoup

for year in range(4,-1,-1):
    
    year=2022-year

    res = requests.get("https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    names = soup.find_all("a", attrs={"class":"tit_main"})

    names_idx2=0

    for idx, image in enumerate(images):
        # 2022년 상위 5개 영화
        if idx >= 5:
            break

        names = str(names)
        names_idx1 = names.index(">", names_idx2)+2
        names_idx2 = names.index("<", names_idx1)-1
        name=names[names_idx1:names_idx2]
        print(year, "년", idx+1, "위:", name)
        names_idx1 = names.index(">", names_idx2)
        names_idx2 = names.index("<", names_idx1)

        image_res = requests.get(image["src"])
        image_res.raise_for_status()

        #print(year, "년", idx+1, "위:", name)

        with open(f"./movies/movie{year}-{idx+1}위.jpg", "wb") as f:
            f.write(image_res.content)

        with open("./movies/최근 5년 연도별 영화 순위 Top5.txt", "a") as f:
            f.write(f"{year}년 {idx+1}위: {name}\n")

    print(year, "년 영화 수:", idx, "\n")

    with open("./movies/최근 5년 연도별 영화 순위 Top5.txt", "a") as f:
            f.write("-------------------\n")