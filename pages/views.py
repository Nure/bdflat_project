from django.shortcuts import render

from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, division_choices

from listings.models import Listing
from agents.models import Agent

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
      'listings': listings,
      'price_choices': price_choices,
      'bedroom_choices': bedroom_choices,
      'division_choices': division_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    #Get all agents
    agents = Agent.objects.order_by('-hire_date')

    #Get MVP
    mvp_agents = Agent.objects.all().filter(is_mvp=True)

    context = {
      'agents': agents,
      'mvp_agents': mvp_agents
    }
    return render(request, 'pages/about.html', context)
