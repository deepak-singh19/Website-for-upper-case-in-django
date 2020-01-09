from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'temp/index.html')

def processed(request):
    if request.method=='POST':
        text=request.POST['text']
        processed=text.upper()
    return HttpResponse(processed)