from typing import List

import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modules.models import Module, Lesson


@pytest.fixture
def modules(db):
    return mommy.make(Module, 2)


@pytest.fixture
def lessons(modules):
    lessons = []
    for module in modules:
        lessons.extend(mommy.make(Lesson, 3, module=module))
    return lessons


@pytest.fixture
def resp(client, modules, lessons):
    resp = client.get(reverse('modules:index'))
    return resp


def test_index_available(resp):
    assert resp.status_code == 200


def test_title(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.title)


def test_description(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.description)


def test_public(resp, modules: List[Module]):
    for module in modules:
        assert_contains(resp, module.public)


def test_lesson_title(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.title)


def test_lesson_link(resp, lessons: List[Lesson]):
    for lesson in lessons:
        assert_contains(resp, lesson.get_absolute_url())
