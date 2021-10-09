from django.shortcuts import render


def index(request):
    name = 'Baikabylova Begimai'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'Djusupov Uson '
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Mamytova Aizura'
    return render(request, 'index3.html', locals())

def index4(request):
    name = 'Baikabylov Omurbek'
    return render(request, 'index4.html', locals())

def index5(request):
    name = 'Baikabylov Nurelbek'
    return render(request, 'index5.html', locals())