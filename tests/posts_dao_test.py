import pytest
from dao.posts_dao import PostsDAO
from config import Config

PATH = Config.POSTS_PATH


class TestPostsDAO:
    def test_load_data(self):
        posts = PostsDAO(PATH)
        assert type(posts.load_data()) == list

    def test_init_file_error(self):
        with pytest.raises(FileNotFoundError):
            PostsDAO("lol.json").load_data()

    def test_get_all(self):
        posts = PostsDAO(PATH)
        assert type(posts.get_all()) == list

    def test_get_by_user(self):
        posts = PostsDAO(PATH)
        for post in posts.load_data():
            assert posts.get_by_user(post.poster_name)

    def test_get_by_user_value_error(self):
        posts = PostsDAO(PATH)
        with pytest.raises(ValueError):
            posts.get_by_user("3gy2jh54hj6jk32k2n52")

    def test_search(self):
        posts = PostsDAO(PATH)
        for post in posts.load_data():
            assert post.content[:4] in posts.search(post.content[:4])[0].content

    def test_get_by_pk(self):
        posts = PostsDAO(PATH)
        assert posts.get_by_pk(1)

    def test_get_by_pk_error(self):
        posts = PostsDAO(PATH)
        with pytest.raises(ValueError):
            posts.get_by_pk(-1)
