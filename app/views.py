from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from app.models import Link

@login_required
def index(request):
    context={}
    context["links"] = Link.objects.all()
    return render(request, 'index.html',context)


def status(request,id):
    if request.method == "POST":
        request = requests.get(Link.objects.filter(id=id, active=True).last().link)
        return JsonResponse({
            "status_code": request.status_code
        })

def update(request,id,interval):
    if request.method =="POST":
        update = Link.objects.filter(id=id).update(interval=interval)
        return JsonResponse({
            "result": "ok"
        })

def active(request,id):
    if request.method =="POST":
        status = not Link.objects.filter(id=id).last().active
        update = Link.objects.filter(id=id).update(active=status)
        return JsonResponse({
            "status": status
        })