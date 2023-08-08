import json

from config import Config
from dao.posts_dao import PostsDAO


class Bookmarks:
    """Класс закладок"""

    def __init__(self):
        """Сразу после инициализации сохраняем список номеров постов"""
        self.path = Config.BOOKMARKS_PATH
        with open(self.path, "r", encoding="utf-8") as file:
            self.posts_pk = json.load(file)

    def get_bookmarks(self):
        """Получаем посты по номерам"""
        bookmarks = []
        for post in PostsDAO().load_data():
            if post.pk in self.posts_pk:
                bookmarks.append(post)
        return bookmarks

    def get_count(self):
        """Получаем количество постов"""
        return len(self.posts_pk)  # именно из-за этой фичи был сделан этот класс

    def append(self, pk):
        """Добавление с записью в файл"""
        if pk not in self.posts_pk:
            self.posts_pk.append(pk)
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(self.posts_pk, file, ensure_ascii=False)

    def delete(self, pk):
        """Удаление с записью в файл"""
        self.posts_pk.remove(pk)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.posts_pk, file, ensure_ascii=False)
