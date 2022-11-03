import pytest

from ads.models import Comment


@pytest.mark.django_db
def test_comment_delete(user_client, user_api, ad):
    comment = Comment.objects.create(ad=ad, author=user_api)

    response = user_client.delete(f"/api/ads/{ad.pk}/comments/{comment.pk}/")

    assert response.status_code == 204


@pytest.mark.django_db
def test_comment_admin_delete(api_admin_client, user_api, ad):
    comment = Comment.objects.create(ad=ad, author=user_api)

    response = api_admin_client.delete(f"/api/ads/{ad.pk}/comments/{comment.pk}/")

    assert response.status_code == 204
