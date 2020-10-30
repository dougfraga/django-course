from django.shortcuts import render

from pypro.modules import facade


def index(request):
    ctx = {'modules': facade.list_modules_with_lessons()}
    return render(request, 'modules/index.html', ctx)


def detail(request, slug):
    module = facade.find_module(slug)
    lessons = facade.list_sorted_module_lessons(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lessons': lessons})


def lesson(request, slug):
    lesson = facade.find_lesson(slug)
    return render(request, 'modules/lesson_detail.html', {'lesson': lesson})
