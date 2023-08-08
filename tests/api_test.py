from app import app


def test_api_posts():
    response = app.test_client().get("/api/posts")
    assert response.status_code == 200
    assert type(response.json) == list
    for post in response.json:
        assert type(post) == dict
        assert post.get("poster_name")
        assert post.get("poster_avatar")
        assert post.get("pic")
        assert post.get("content")
        assert post.get("views_count")
        assert post.get("likes_count")
        assert post.get("pk")


def test_api_post():
    response = app.test_client().get("/api/posts/1")
    assert response.status_code == 200
    assert type(response.json) == dict
    post = response.json
    assert post.get("poster_name")
    assert post.get("poster_avatar")
    assert post.get("pic")
    assert post.get("content")
    assert post.get("views_count")
    assert post.get("likes_count")
    assert post.get("pk")
