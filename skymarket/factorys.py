import factory

from ads.models import Ad, Comment
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "test name"
    last_name = "test last_name"
    phone = "+79993704028"
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    title = "test title"
    price = 1000
    description = "test description"
    author = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = "test text"
    author = factory.SubFactory(UserFactory)
    ad = factory.SubFactory(AdFactory)
