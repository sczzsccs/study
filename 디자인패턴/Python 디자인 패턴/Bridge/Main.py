from Draft import*
from SimpleDisplay import*
from CaptionDisplay import*
from Publication import*

Title = "제목"
Author = "저자"
Content = {
    "내용1", 
    "내용2", 
    "내용3"
}

draft = Draft(Title, Author, Content)
draft.display(SimpleDisplay())
print()
draft.display(CaptionDisplay())
print()

Publisher = "북악출판"
cost = 100
publi = Publication(draft, Publisher, cost)

publi.display(SimpleDisplay())
print()
publi.display(CaptionDisplay())