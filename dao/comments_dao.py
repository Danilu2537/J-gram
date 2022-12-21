import json
from dao.classes import Comment


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
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
        comments = []
        for comment in self.load_data():
            if post_id == comment.post_id:
                comments.append(comment)
        return comments
