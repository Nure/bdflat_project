from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .choices import price_choices, bedroom_choices, division_choices


from .models import Listing 

# Create your views here.
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
      'listings': paged_listings,
      'price_choices': price_choices,
      'bedroom_choices': bedroom_choices,
      'division_choices': division_choices
  }
  return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context)


def search(request):
  query_list = Listing.objects.order_by('-list_date')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_list = query_list.filter(description__icontains=keywords)
  
  #city
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      query_list = query_list.filter(city__iexact=city)
  
  #division
  if 'division' in request.GET:
    division = request.GET['division']
    if division:
      query_list = query_list.filter(division__iexact=division)

  #bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      query_list = query_list.filter(bedrooms__lte=bedrooms)
  #price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      query_list = query_list.filter(price__lte=price)
  context = {
    'division_choices': division_choices,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
    'listings' : query_list,
    'values' : request.GET
  }
  return render(request, 'listings/search.html', context)
