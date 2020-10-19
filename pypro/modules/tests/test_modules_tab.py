import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modules.models import Module


@pytest.fixture
def modules(db):
    return mommy.make(Module, 2)


@pytest.fixture
def resp(client, modules):
    resp = client.get(reverse('base:home'))
    return resp


def test_email_link(resp, modules):
    for module in modules:
        assert_contains(resp, module.title)
