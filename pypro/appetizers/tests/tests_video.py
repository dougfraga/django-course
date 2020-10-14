import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('appetizers:video', args=('motivation',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, 'Appetizer Video: Motivation')


def test_video_content(resp):
    assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/93J_ZDruRM4"')
