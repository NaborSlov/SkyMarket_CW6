import pytest

from factorys import CommentFactory


@pytest.mark.django_db
def test_comment_detail(user_client, ad, user_api):
    comment = CommentFactory.create(ad=ad, author=user_api)

    response = user_client.get(f"/api/ads/{ad.pk}/comments/{comment.pk}/")

    expected_response = {
        "pk": comment.pk,
        "text": "test text",
        "author_id": user_api.pk,
        "created_at": response.data.get("created_at"),
        "author_first_name": user_api.first_name,
        "author_last_name": user_api.last_name,
        "ad_id": ad.pk,
        "author_image": None
    }

    assert response.status_code == 200
    assert response.data == expected_response
