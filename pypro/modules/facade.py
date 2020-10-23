from typing import List

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
    return Lesson.objects.get(slug=slug)
