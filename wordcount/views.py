from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {"dict_key": "dict_value"})


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_counter = {word: word_list.count(word) for word in word_list}
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'word_count': word_counter})


def about(request):
    return render(request, "about.html")
