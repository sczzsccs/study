from DisplayArticleTemplate import*
class CaptionDisplayArticle(DisplayArticleTemplate):
    def __init__(this, article:Article):
        super().__init__(article)

    def title(this)->None:
        print(f"Title: {this.article.gatTitle()}")
    
    def content(this)->None:
        print(f"Content:")
        for item in this.article.gatContent():
            print(f"\t{item}")
    
    def footer(this)->None:
        print(f"Footer: {this.article.gatFooter()}")
    pass