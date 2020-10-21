from typing import List

from pypro.modules.models import Module


def list_sorted_modules() -> List[Module]:
    """
    List modules sorted by title
    :return
    """
    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)
