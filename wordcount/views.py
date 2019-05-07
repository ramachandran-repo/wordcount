from django.shortcuts import render
from datetime import datetime
from dateutil import relativedelta

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


def datecalc(request):
    date_text = request.GET['date']
    today = datetime.now().date()
    given_date = datetime.strptime(date_text, '%Y-%m-%d').date()
    calc_date = relativedelta.relativedelta(today, given_date)
    value_dict = {'currentDate': str(today), 'enteredDate': str(given_date), 'calculatedDate': calc_date}
    return render(request, "calculate.html", value_dict)


def agecalculator(request):
    return render(request, 'agecalculator.html')


def wordcounter(request):
    return render(request, 'wordcounter.html')

