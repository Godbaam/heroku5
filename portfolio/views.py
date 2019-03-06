from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

# Create your views here.
