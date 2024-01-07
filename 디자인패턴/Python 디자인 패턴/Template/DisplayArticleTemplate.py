from abc import*
from Article import*
class DisplayArticleTemplate(metaclass=ABCMeta):
    @abstractmethod
    def title(this)->None:pass
    @abstractmethod
    def content(this)->None:pass
    @abstractmethod
    def footer(this)->None:pass
    
    @abstractmethod
    def __init__(this, article:Article):
        this.article = article
    
    def display(this):
        this.title()
        this.content()
        this.footer()
    pass