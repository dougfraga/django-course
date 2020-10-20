import pytest
from model_mommy import mommy

from pypro.modules import facade
from pypro.modules.models import Module


@pytest.fixture
def modules(db):
    return [mommy.make(Module, title=s) for s in 'antes depois'.split()]


def test_list_sorted_modules(modules):
    assert list(sorted(modules, key=lambda module: module.title)) == facade.list_sorted_modules()
