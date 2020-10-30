from typing import List

from django.db.models import Prefetch

from pypro.modules.models import Module, Lesson


def list_sorted_modules() -> List[Module]:
    """
    List modules sorted by title
    :return
    """
    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def list_sorted_module_lessons(module: Module):
    return list(module.lesson_set.order_by('order').all())


def find_lesson(slug):
    return Lesson.objects.select_related('module').get(slug=slug)


def list_modules_with_lessons():
    sorted_lessons = Lesson.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(Prefetch(
        'lesson_set', queryset=sorted_lessons, to_attr='lessons')
    ).all()
