import requests
from posts import Posts
from config import * 

class Bludit:
    # compilacoes = "https://compilacoes.nasajon.com.br/wp-json/wp/v2/posts"
    compilacoes = "http://localhost:8000"

    def doPost(self, post: Posts):
        post.authentication = AUTHENTICATION
        post.tokenApi = TOKEN_API

        requests.post(self.compilacoes, data=post)
