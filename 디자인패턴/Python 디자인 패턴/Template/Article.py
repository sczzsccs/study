class Article:
    def __init__(this, title, content, footer) -> None:
        this.title = title
        this.content = content
        this.footer = footer
        pass
    
    def gatTitle(this)->str:
        return this.title
    
    def gatContent(this)->list:
        return this.content
    
    def gatFooter(this)->str:
        return this.footer
    pass