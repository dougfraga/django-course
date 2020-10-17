from django.shortcuts import render, get_object_or_404

from pypro.appetizers.models import Video

videos = [
    Video(slug='motivation', title='Appetizer Video: Motivation', youtube_id='93J_ZDruRM4'),
    Video(slug='piano', title='Piano sample', youtube_id='vhJNpOkJFkc')
]

videos_dct = {v.slug: v for v in videos}


def index(request):
    return render(request, 'appetizers/index.html', context={'videos': videos})


def video(request, slug):
    v = get_object_or_404(Video, slug=slug)
    return render(request, 'appetizers/video.html', context={'video': v})
