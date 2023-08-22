from django.shortcuts import render

# Create your views here.


def portfolio(request, name):
    user = {'name': name}
    return render(request, 'portfolio/portfolio.html', user)
