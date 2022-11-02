import pytest


@pytest.mark.django_db
def test_create_comment(user_client, ad, user_api):
    data = {
        "text": "test text"
    }

    response = user_client.post(f"/api/ads/{ad.pk}/comments/", data)

    expected_response = {
        "pk": response.data.get("pk"),
        "text": "test text",
        "author_id": user_api.pk,
        "created_at": response.data.get("created_at"),
        "ad_id": ad.pk
    }

    assert response.status_code == 201
    assert response.data == expected_response
