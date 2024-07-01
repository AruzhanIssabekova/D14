from django.http import HttpResponse

def main(request):
    return HttpResponse("Second App Main Page")

def services(request):
    return HttpResponse("Our Services")

def portfolio(request):
    return HttpResponse("Our Portfolio")
