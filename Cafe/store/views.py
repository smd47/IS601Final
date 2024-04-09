from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html',context)

def menu(request):
    context = {}
    return render(request, 'menu.html',context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html',context)

def thankyou(request):
    context = {}
    return render(request, 'thankyou.html',context)