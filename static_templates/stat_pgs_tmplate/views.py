from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'home.html', ctx)

@login_required
def contact(request):
    return render(request, 'contact.html')


def p1(request):
    body = {
        'user': "John",
        'login': True,
        'password_length': 16
    }
    return render(request, 'page1.html', body)

def p2(request):
    content2 = {
        'list1': [1, 2, 100, 200],
        'dict1': {"A": 1, "B": 2, "C": 3, "D": 4, "E": 3}
    }
    return render(request, 'page2.html', content2)

