from django.shortcuts import render , HttpResponse
from galaxy_app.models import Review
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("HomePage")

def playGames(request):
    return render(request,'playgames.html')

def books(request):
    return render(request,'books.html')

def spaceworks(request):
    return render(request,'space.html')

def review(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname =  request.POST.get('lastname')
        phone    =  request.POST.get('phone')
        address  =  request.POST.get('Address')
        city     =  request.POST.get('City')
        state    =  request.POST.get('State')
        desc  =     request.POST.get('desc')
        r        =  Review(firstname=firstname , lastname=lastname , phone=phone , address=address , city=city , state=state , desc=desc)
        r.save()
        messages.success(request, "Your response is submitted successfully!")
    return render(request,'Review.html')