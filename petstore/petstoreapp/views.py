from django.shortcuts import render, redirect
from . models import Pet
from . forms import *
# Create your views here.
def index(r):
    petdata = Pet.objects.all()
    context = {"petdata": petdata}
    return render(r, "index.html", context)


def petdetails(req, sent_petid):
    singlepet = Pet.objects.get(petid=sent_petid)
    context = {"singlepet": singlepet}
    return render(req, "petdetailpage.html", context)


def addnewpet(req):
    if req.method == "GET":
        context = {}
        form = RegisterNewPet()
        context["form"] = form
        return render(req, "newpet.html", context)
    else:
        context = {}
        form = RegisterNewPet(req.POST, req.FILES or None)
        if form.is_valid():
            form.save()
        context["form"] = form
        return redirect("/")