from dao.comments_dao import CommentsDAO


class TestCommentsDAO:
    def test_load_data(self):
        comments = CommentsDAO()
        assert type(comments.load_data()) == list

    def test_get_by_id(self):
        comments = CommentsDAO()
        assert comments.get_by_post_id(1)
