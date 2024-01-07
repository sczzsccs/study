from Display import*
from Draft import*
class CaptionDisplay(Display):
    def __init__(self) -> None:
        print("[Style - CaptionDisplay]")
    
    def title(this, draft:Draft):
        print(f"Title: {draft.getTitle()}")

    def author(this, draft:Draft):
        print(f"Author: {draft.getAuthor()}")

    def content(this, draft:Draft):
        print("Content:")
        for item in draft.getContent():
            print(f"\t{item}")
    pass