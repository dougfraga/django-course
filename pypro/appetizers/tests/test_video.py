import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.appetizers.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('appetizers:video', args=(video.slug,)))


@pytest.fixture
def resp_video_not_found(client, video):
    return client.get(reverse('appetizers:video', args=(f'{video.slug}video_not_found',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_page_not_found(resp_video_not_found):
    assert resp_video_not_found.status_code == 404


def test_video_title(resp, video):
    assert_contains(resp, video.title)


def test_video_content(resp, video):
    assert_contains(resp, f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video.youtube_id}"')
