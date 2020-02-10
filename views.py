from django.shortcuts import render,redirect 
from django.utils.crypto import get_random_string 

def index(request):
    context = {
        "random_string": get_random_string(length=14)
    }

    if not "counter" in request.session:
        request.session["counter"] = 0
    request.session["counter"] += 1
    return render(request, "index.html", context)

def reset(request):
    request.session.clear()
    return redirect ("/")
