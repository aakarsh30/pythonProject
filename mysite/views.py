from django.shortcuts import render


def index(request):
    count = 0
    return render(request, 'index.html', {'counter': count})

#
# def subs(request):
#     return render(request, 'subs.html')