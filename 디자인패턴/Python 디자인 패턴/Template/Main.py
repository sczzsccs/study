from Article import*
from SimpleDisplayArticle import*
from CaptionDisplayArticle import*

Title = "디자인패턴"
Content = []
Content.append("디자인패턴은 클래스 간의 효율적이고 최적화된 관계를 설계하는 것입니다.")
Content.append("각 패턴을 외우기 보다 이해하는 것이 중요합니다.")
Content.append("다양한 패턴을 접하고 반복적으로 이해할수록")
Content.append("각 디자인패턴에 대한 응용의 폭이 넓어질 것입니다.")
Footer = "2022.01.09, GIS Developer 김형준"

article = Article(title=Title, content= Content, footer=Footer)

print("[STYLE - SimpleDisplayArticle]")
style1 = SimpleDisplayArticle(article)
style1.display()

print("\n[STYLE - CaptionDisplayArticle]")
style2 = CaptionDisplayArticle(article)
style2.display()