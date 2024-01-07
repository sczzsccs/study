from Display import*

class Draft():
    def __init__(this, title:str, author:str, content:list) -> None:
        this.title = title
        this.author = author
        this.content = content
        pass
    
    def getTitle(this): return this.title
    def getAuthor(this): return this.author
    def getContent(this): return this.content
    
    def display(this, display: Display) -> None:
        display.title(this)
        display.author(this)
        display.content(this)
    pass