import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from factorys import UserFactory, AdFactory, CommentFactory
from users.models import User

register(UserFactory)
register(AdFactory)
register(CommentFactory)


@pytest.fixture
def user_api(db):
    user = User.objects.create_user(
        first_name="test name",
        last_name="test last_name",
        email="test@mail.ru",
        phone="+79224846016"
    )

    return user


@pytest.fixture
def user_client(user_api):
    client = APIClient()
    token = RefreshToken.for_user(user_api)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client


@pytest.fixture
def admin_api(db):
    user = User.objects.create_superuser(
        first_name="test name admin",
        last_name="test last_name admin",
        email="testadmin@mail.ru",
        phone="+79224846016"
    )

    return user


@pytest.fixture
def api_admin_client(admin_api):
    client = APIClient()
    token = RefreshToken.for_user(admin_api)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client
