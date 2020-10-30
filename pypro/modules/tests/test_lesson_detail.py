import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modules.models import Module, Lesson


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def lesson(module):
    return mommy.make(Lesson, module=module)


@pytest.fixture
def resp(client, lesson):
    resp = client.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_title(resp, lesson: Lesson):
    assert_contains(resp, lesson.title)


def test_video(resp, lesson: Lesson):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{lesson.youtube_id}"')


def test_module_breadcrumb_title(resp, module: Module):
    assert_contains(resp, f'{module.title}</a></li>')


def test_module_breadcrumb_url(resp, module: Module):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{module.get_absolute_url()}')
