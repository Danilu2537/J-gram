import json
from config import Config
from dao.classes import Post


class PostsDAO:
    def __init__(self):
        self.path = Config.POSTS_PATH

    def load_data(self):
        with open(self.path, "r", encoding='utf-8') as file:
            posts_data = json.load(file)
            posts = []

            for post in posts_data:
                content = []
                for word in post['content'].split():
                    if word[0] == '#':
                        content.append(f'<a href="/tag/{word[1:]}" class="item__tag">{word}</a>')
                    else:
                        content.append(word)
                posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    " ".join(content),
                    post['views_count'],
                    post['likes_count'],
                    post['pk']
                ))
            return posts

    def get_all(self):
        return self.load_data()

    def get_by_user(self, user_name):
        posts = []
        for post in self.load_data():
            if user_name in post.poster_name:
                posts.append(post)
        if posts:
            return posts
        raise ValueError("Нет постов такого пользователя")

    def search(self, query):
        posts = []
        for post in self.load_data():
            if query.lower() in post.content.lower():
                posts.append(post)
        return posts

    def get_by_pk(self, pk):
        for post in self.load_data():
            if pk == post.pk:
                return post
        raise ValueError("Такого поста нет")
