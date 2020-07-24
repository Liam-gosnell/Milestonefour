from django.shortcuts import render, get_object_or_404
from .models import Portfolio

# Create your views here.

def all_portfolio(request):
    """ A view to return the index page """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'portfolio/portfolio.html', context)


def portfolio_details(request, portfolio_id):
    """ A view single portfolio details"""

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio_details.html', context)