from django.shortcuts import render


def index(request):
    args = dict()
    return render(request, 'index.html', args)
