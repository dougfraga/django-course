from django.shortcuts import render

from pypro.modules import facade


def detail(request, slug):
    module = facade.find_module(slug)
    lessons = facade.list_sorted_module_lessons(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lessons': lessons})


def lesson(request, slug):
    lesson = facade.find_lesson(slug)
    return render(request, 'modules/lesson_detail.html', {'lesson': lesson})
