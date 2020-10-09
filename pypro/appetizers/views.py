from django.shortcuts import render

def video(request, slug):
    return render(request, 'appetizers/video.html')
