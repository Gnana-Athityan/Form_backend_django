from os import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from first.models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        know = request.POST.get('know')
        review = request.POST.get('review')
        contact = Contact(name = name , age = age, know = know, review = review , date=datetime.today())
        contact.save()
        messages.success(request, 'Details updated successfully.')
        
    #return HttpResponse("This is a contact page")
    return render(request ,'contact.html')
