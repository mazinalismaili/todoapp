from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):

    #return HttpResponse("Hello world")
    context = {
        'Name':'Mazin',
        'Age':'25',
    }
    return render(request, 'index.html',context=context)