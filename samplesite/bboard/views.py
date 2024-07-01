from django.http import HttpResponse

def index(request):
    return HttpResponse("Bulletin Board Index Page")

def detail(request, item_id):
    return HttpResponse(f"Detail of Item {item_id}")

def add(request):
    return HttpResponse("Add New Item")

