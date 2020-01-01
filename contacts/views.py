from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    agent_email = request.POST['agent_email']


    #check id user has made inquery already

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id)

      if has_contacted:
        messages.error(request, 'You have already made an inquery for this Flat/Apartment')
        return redirect('/listings/' + listing_id)
    
    
    contact = Contact(listing=listing, listing_id=listing_id, name=name,
                      email=email, phone=phone, message=message, user_id=user_id)
    contact.save()
    messages.success(request, 'Thanks for your request!, one of our agent will get back to you!')

    # Send mail
    send_mail(
        'Flat/Apartment Inquery',
        'You made an inquery for ' + listing + '. Sign in for more info',
        'nalamsiddiq@gmail.com',
        [agent_email, 'me@nuresiddiq.com'],
        fail_silently=True
    )
    return redirect('/listings/' + listing_id)
