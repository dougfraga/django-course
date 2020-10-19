from pypro.modules import facade


def list_modules(request):
    return {'MODULES': facade.list_sorted_modules()}