from Draft import*
class Publication(Draft):
    def __init__(this, title:str, author:str, content:list, publisher:str, cost:int) -> None:
        this.title = title
        this.author = author
        this.content = content
        this.publisher = publisher
        this.cost = cost
        pass
    
    def __init__(this, darft:Draft, publisher:str, cost:int) -> None:
        super().__init__(title=darft.getTitle(), author=darft.getAuthor(), content=darft.getContent())
        this.publisher = publisher
        this.cost = cost
        pass

    def display(this, display: Display) -> None:
        super().display(display=display)
        print(f"#{this.publisher}, ${this.cost}")
    pass