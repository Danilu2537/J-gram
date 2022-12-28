import json
from dao.posts_dao import PostsDAO
from config import Config


class Bookmarks:
    def __init__(self):
        self.path = Config.BOOKMARKS_PATH
        with open(self.path, "r", encoding='utf-8') as file:
            self.posts_pk = json.load(file)

    def get_bookmarks(self):
        bookmarks = []
        for post in PostsDAO().load_data():
            if post.pk in self.posts_pk:
                bookmarks.append(post)
        return bookmarks

    def get_count(self):
        return len(self.posts_pk)

    def append(self, pk):
        if pk not in self.posts_pk:
            self.posts_pk.append(pk)
            with open(self.path, "w", encoding='utf-8') as file:
                json.dump(self.posts_pk, file, ensure_ascii=False)

    def delete(self, pk):
        self.posts_pk.remove(pk)
        with open(self.path, "w", encoding='utf-8') as file:
            json.dump(self.posts_pk, file, ensure_ascii=False)
