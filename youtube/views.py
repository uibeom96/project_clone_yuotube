from django.shortcuts import render


def index(request):
    return render(request, "youtube/index.html")


def detail(request):
    return render(request, "youtube/detail.html")