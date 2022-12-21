import pytest
from dao.comments_dao import CommentsDAO
from config import Config

PATH = Config.COMMENTS_PATH


class TestCommentsDAO:
    def test_load_data(self):
        comments = CommentsDAO(PATH)
        assert type(comments.load_data()) == list

    def test_get_by_id(self):
        comments = CommentsDAO(PATH)
        assert comments.get_by_post_id(1)
