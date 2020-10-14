import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('appetizers:index'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    [
        'Appetizer Video: Motivation',
        'Piano sample'
    ]
)
def test_video_title(resp, title):
    assert_contains(resp, title)


@pytest.mark.parametrize(
    'slug',
    [
        'motivation',
        'piano'
    ]
)
def test_link_title(resp, slug):
    video_link = reverse('appetizers:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
