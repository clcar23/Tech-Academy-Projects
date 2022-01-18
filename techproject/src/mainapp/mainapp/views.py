from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    user = request.user
    context = {
        "user": user, #this is a dictionary obj with a key/value pair
    }
    return render(request, "home.html", context) #using render to 'render' it to the website