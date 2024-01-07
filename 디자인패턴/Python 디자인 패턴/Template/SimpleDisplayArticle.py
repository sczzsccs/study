from DisplayArticleTemplate import*
from Article import*
class SimpleDisplayArticle(DisplayArticleTemplate):
    def __init__(this, article:Article):
        super().__init__(article)

    def title(this)->None:
        print(this.article.gatTitle())
    
    def content(this)->None:
        for item in this.article.gatContent():
            print(item)
    
    def footer(this)->None:
        print(this.article.gatFooter())
    pass