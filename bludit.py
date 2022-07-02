import requests
from posts import Posts
from config import * 

class Bludit(Posts):
    def __init__(self, authentication, tokenApi, title, content, slug, categories, status="publish"):
        super().__init__(title, content, slug, categories, status)
        self.__authentication = authentication
        self.__tokenApi = tokenApi

    
    def doPost(self):
        data = {
            'token': self.__tokenApi,
            'authentication': self.__authentication,
            'title': self.title,
            'content': self.content,
            'slug': self.slug,
            'categories': self.categories
        }

        post = requests.post(BASE_URL, data= data)

        return post
