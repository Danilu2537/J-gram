import pytest
from dao.posts_dao import PostsDAO


class TestPostsDAO:
    def test_init_file_error(self):
        with pytest.raises(FileNotFoundError):
            posts = PostsDAO()
            posts.path = "lol.json"
            posts.load_data()

    def test_load_data(self):
        posts = PostsDAO()
        assert type(posts.load_data()) == list

    def test_get_all(self):
        posts = PostsDAO()
        assert type(posts.get_all()) == list

    def test_get_by_user(self):
        posts = PostsDAO()
        for post in posts.load_data():
            assert posts.get_by_user(post.poster_name)

    def test_get_by_user_value_error(self):
        posts = PostsDAO()
        with pytest.raises(ValueError):
            posts.get_by_user("3gy2jh54hj6jk32k2n52")

    def test_search(self):
        posts = PostsDAO()
        for post in posts.load_data():
            assert post.content[:4].lower() in posts.search(post.content[:4])[0].content.lower()

    def test_get_by_pk(self):
        posts = PostsDAO()
        assert posts.get_by_pk(1)

    def test_get_by_pk_error(self):
        posts = PostsDAO()
        with pytest.raises(ValueError):
            posts.get_by_pk(-1)
