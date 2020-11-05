import pytest
from model_mommy import mommy


@pytest.fixture
def logged_user(db, django_user_model):
    user_sample = mommy.make(django_user_model, first_name='Fulano')
    return user_sample


@pytest.fixture
def client_with_logged_user(logged_user, client):
    client.force_login(logged_user)
    return client
