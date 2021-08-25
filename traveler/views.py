from django.shortcuts import render,get_object_or_404
from traveler import models
from django.http import HttpResponse, HttpResponseRedirect,Http404, response
# Create your views here.
def index(request):
    places=models.Place.objects.all()
    # print(places)
    # print(places[0:4])
    context={
        'top4_places':places[0:4]
    }
    response=render(request,'traveler/index.html',context)
    return response

def listPlaces(request):
    places=models.Place.objects.all()
    context={
        'places':places
    }
    response=render(request,'traveler/list.html',context)
    return response

def search(request):
    places=models.Place.objects.all()
    # print(places)
    # print(places[0:4])
    context={
        'top4_places':places[0:4]
    }
    if 'place' in request.GET:
        place=request.GET['place']
        print("place is",place)
        if place:
            if place=="":
                return render(request,'traveler/index.html',context=context)
            try:
                places_possible=models.Place.objects.get(name__icontains=place)
                print(places_possible)
                return HttpResponseRedirect('/detail/'+ str(places_possible.pk))
            except Exception as e:
                print(e)
                context['error']='No Such Record In Our Database. Sorry!!'
                return render(request,'traveler/index.html',context=context)
    return render(request,'traveler/index.html')

def detail(request,pk):
    # return render(request,'traveler/detail.html')
    place=get_object_or_404(models.Place,pk=pk)
    context={
        'place':place
    }
    return render(request,'traveler/detail.html',context=context)