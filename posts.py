class Posts:
    def __init__(self, title, content, slug, categories, status = "publish"):
        self.title = title
        self.content = content
        self.slug = slug
        self.status = status
        self.categories = categories
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
    
    @property
    def slug(self):
        return self.__slug
    
    @slug.setter
    def slug(self, link):
        self.__slug = link

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, categories):
        self.__categories = categories