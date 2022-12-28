class Post:
    """Класс поста с атрибутами"""
    def __init__(self, poster_name, poster_avatar, pic, content,
                 views_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"Пост {self.poster_name}, id {self.pk}"


class Comment:
    """Класс комментария с атрибутами"""
    def __init__(self, post_id, commenter_name,
                 comment, pk):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

    def __repr__(self):
        return f"Комментарий к посту {self.post_id}"
