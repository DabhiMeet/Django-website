from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import mission
import datetime

def index(request):
    # m1 = mission()
    # m1.name = 'Mars Mission'
    # m1.img = 'finding-planet.jpg'
    # m1.date = datetime.date(2021,2,20)
    
    
    # m2 = mission()
    # m2.name = 'Satellite PSLV'
    # m2.img = 'new-satellitedish.jpg'
    # m2.date = datetime.date(2021,2,22)


    # miss = [m1,m2]

    miss = mission.objects.all()


    return render(request,"index.html",{'miss':miss})
