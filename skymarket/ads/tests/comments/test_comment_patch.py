import pytest

from ads.models import Comment


@pytest.mark.django_db
def test_comment_patch(user_client, user_api, ad):
    comment = Comment.objects.create(text="text", ad=ad, author=user_api)

    response = user_client.patch(f"/api/ads/{ad.pk}/comments/{comment.pk}/", {"text": "text test patch"})

    expected_response = {
        "pk": comment.pk,
        "text": "text test patch",
        "author_id": user_api.pk,
        "created_at": response.data.get("created_at"),
        "author_first_name": user_api.first_name,
        "author_last_name": user_api.last_name,
        "ad_id": ad.pk,
        "author_image": None
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_comment_admin_patch(api_admin_client, user_api, ad):
    comment = Comment.objects.create(text="text", ad=ad, author=user_api)

    response = api_admin_client.patch(f"/api/ads/{ad.pk}/comments/{comment.pk}/", {"text": "text test patch"})

    expected_response = {
        "pk": comment.pk,
        "text": "text test patch",
        "author_id": user_api.pk,
        "created_at": response.data.get("created_at"),
        "author_first_name": user_api.first_name,
        "author_last_name": user_api.last_name,
        "ad_id": ad.pk,
        "author_image": None
    }

    assert response.status_code == 200
    assert response.data == expected_response
