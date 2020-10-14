from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, youtube_id):
        self.slug = slug
        self.title = title
        self.youtube_id = youtube_id

    def get_absolute_url(self):
        return reverse('appetizers:video', args=(self.slug,))


videos = [
    Video('motivation', 'Appetizer Video: Motivation', '93J_ZDruRM4'),
    Video('piano', 'Piano sample', 'vhJNpOkJFkc')
]

videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    v = videos_dct[slug]
    return render(request, 'appetizers/video.html', context={'video': v})
