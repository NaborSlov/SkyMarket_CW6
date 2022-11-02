import pytest

from ads.serializers import CommentSerializer
from factorys import CommentFactory


@pytest.mark.django_db
def test_comment_list(user_client, ad):
    comments = CommentFactory.create_batch(9, ad=ad)

    expected_response = {
        "count": 9,
        "next": None,
        "previous": None,
        "results": CommentSerializer(comments, many=True).data[::-1]
    }

    response = user_client.get(f"/api/ads/{ad.pk}/comments/")

    assert response.status_code == 200
    assert response.data == expected_response
