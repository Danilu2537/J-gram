import json
from config import Config
from dao.classes import Comment


class CommentsDAO:
    """Класс получения комментариев, аналогичен PostsDAO"""
    def __init__(self):
        self.path = Config.COMMENTS_PATH

    def load_data(self):
        """Создание обьектов комментариев, исходный файл не изменяется"""
        with open(self.path, "r", encoding='utf-8') as file:
            comments_data = json.load(file)
            comments = []

            for comment in comments_data:
                comments.append(Comment(
                    comment['post_id'],
                    comment['commenter_name'],
                    comment['comment'],
                    comment['pk']
                ))
        return comments

    def get_by_post_id(self, post_id):
        """
        Метод получения всех комментариев к определенному посту
        по его порядковому номеру
        """
        comments = []
        for comment in self.load_data():
            if post_id == comment.post_id:
                comments.append(comment)
        return comments
