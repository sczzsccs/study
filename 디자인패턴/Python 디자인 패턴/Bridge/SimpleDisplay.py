from Display import*
from Draft import*
class SimpleDisplay(Display):
    def __init__(self) -> None:
        print("[Style - SimpleDisplay]")
        
    def title(this, draft:Draft):
        print(draft.getTitle())

    def author(this, draft:Draft):
        print(draft.getAuthor())

    def content(this, draft:Draft):
        for item in draft.getContent():
            print(item)
    pass