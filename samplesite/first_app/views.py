from django.http import HttpResponse

def home(request):
    return HttpResponse("First App Home Page")

def about(request):
    return HttpResponse("About First App")

def contact(request):
    return HttpResponse("Contact Page")
