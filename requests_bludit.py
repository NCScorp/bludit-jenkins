import requests
from config import *
from posts import Posts

txt = Posts('teste', 'opa, bão?', 'teste-slug', categories='categoria-teste')

data = {
    'token': TOKEN_API,
    'authentication': AUTHENTICATION,
    'title': txt.title,
    'content': txt.content,
    'slug': txt.slug,
    'categories': txt.categories
}

req_post = requests.post(f'{BASE_URL}/api/pages', data=data)
print(req_post.text)

