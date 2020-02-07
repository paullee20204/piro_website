from django.shortcuts import render


def home(request):
    return render(request, 'main.html')


def recruit(request):
    return render(request, 'internal/recruit.html')


def portfolio(request):
    return render(request, 'internal/port_list.html')