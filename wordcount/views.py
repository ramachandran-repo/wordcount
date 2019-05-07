from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {"dict_key": "dict_value"})


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_counter = {word: word_list.count(word) for word in word_list}
    params = {'fulltext': fulltext, 'count': len(word_list), 'word_count': word_counter, 'numberOfChars': len(fulltext)}
    return render(request, 'count.html', params)


def about(request):
    return render(request, "about.html")


def dateCalc(request):
    date = request.GET['date']
    dates = date.split("-")
    year = 2019-int(dates[0])
    month = 5-int(dates[1])
    datevalue = 11 - int(dates[2])
    return render(request, "calculate.html", {'date': date,'year':year,'month':month,'dateValue':datevalue})

