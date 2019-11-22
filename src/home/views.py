from django.shortcuts import render, redirect


def home(request):
    context = {'title': 'Secret Santa', 'page_description': 'This is the page description'}
    return render(request, 'home.html', context)