Time_loss = {
    "분식집":10,
    "도서관":13,
    "강아지":8
}

root_School = {
    "학교-분식집":10,
    "학교-강아지-집":15+10
}

root_BounSic = {
    "분식집-도서관":3,
    "분식집-강아지-집":10+10
}

root_Library = {
    "도서관-강아지-집":10+10,
    "도서관-집":13
}

if root_BounSic["분식집-도서관"] + root_Library["도서관-집"] >= root_BounSic["분식집-강아지-집"]: root_BounSic_House = root_BounSic["분식집-강아지-집"]
else: root_BounSic_House = root_BounSic["분식집-도서관"] + root_Library["도서관-집"]

print("민준:", root_School["학교-강아지-집"] + Time_loss["강아지"], "분")
print("현우:", root_School["학교-분식집"] + root_BounSic["분식집-강아지-집"] + Time_loss["분식집"] + Time_loss["강아지"], "분")
print("서연:", root_School["학교-분식집"] + root_BounSic["분식집-도서관"] + root_Library["도서관-집"] + Time_loss["분식집"] + Time_loss["도서관"], "분")
print("서윤:", root_School["학교-분식집"] + root_BounSic["분식집-도서관"] + root_Library["도서관-집"] + Time_loss["도서관"], "분")
print("서현:", root_School["학교-분식집"] + root_BounSic_House + Time_loss["분식집"], "분")