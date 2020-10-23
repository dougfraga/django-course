import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modules.models import Module, Lesson


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def lessons(module):
    return mommy.make(Lesson, 3, module=module)


@pytest.fixture
def resp(client, module, lessons):
    resp = client.get(reverse('modules:detail', kwargs={'slug': module.slug}))
    return resp


def test_title(resp, module: Module):
    assert_contains(resp, module.title)


def test_description(resp, module: Module):
    assert_contains(resp, module.description)


def test_public(resp, module: Module):
    assert_contains(resp, module.public)


def test_lesson_title(resp, lessons):
    for lesson in lessons:
        assert_contains(resp, lesson.title)


def test_lesson_link(resp, lessons):
    for lesson in lessons:
        assert_contains(resp, lesson.get_absolute_url())
