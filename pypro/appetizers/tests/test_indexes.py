import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.appetizers.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('appetizers:index'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp, videos):
    for video in videos:
        assert_contains(resp, video.title)


def test_link_title(resp, videos):
    for video in videos:
        video_link = reverse('appetizers:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
