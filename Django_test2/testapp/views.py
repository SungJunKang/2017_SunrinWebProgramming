from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def second(request):
    return render(request,'testapp/second.html')

def third(request):
    return render(request,'testapp/third.html')
