from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def posts_index(request):
    return render(request, "posts/index.html")


def posts_detail(request):
    return render(request, "posts/detail.html")


def deals_index(request):
    return render(request, "deals/index.html")


def thrifts_index(request):
    return render(request, "thrifts/index.html")
