import requests
from bs4 import BeautifulSoup
import csv

file_Name="시가총액1-200.csv"
file=open(file_Name, 'w', encoding="utf-8-sig", newline="")
writer=csv.writer(file)

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for i in range(4):
  res=requests.get(f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={i+1}")
  res.raise_for_status()
  soup=BeautifulSoup(res.text, "lxml")

  table_row=soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

  for row in table_row:
    cols=row.find_all("td")
    if len(cols)<=1:
      continue
    data=[col.getText().strip() for col in cols]
    print(data)
    writer.writerow(data)