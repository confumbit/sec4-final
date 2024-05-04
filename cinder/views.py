from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound

from .models import User


# Create your views here.
def index(request):

    return render(request, "cinder/index.html", {"user_count": User.objects.count()})


def login(request):
    return render(request, "cinder/login.html", {})


def register(request):
    return render(request, "cinder/register.html", {})


def profiles(request):
    users = User.objects.all()
    print(users.count())

    context = {"users": users, "user_count": users.count()}

    return render(request, "cinder/profiles.html", context)


def finishlogin(request):
    try:
        user = User.objects.get(email=request.POST["email"])
        print("woeifn", user)
    except:
        return HttpResponseNotFound("User does not exist")

    if user.password != request.POST["password"]:
        return HttpResponseNotFound("Wrong password")

    return redirect("profiles")


def finishregister(request):
    user = User(
        name=request.POST["name"],
        email=request.POST["email"],
        password=request.POST["password"],
        grade=request.POST["class"],
        section=request.POST["section"],
        gender=request.POST["gender"],
        interests=request.POST["interests"],
        bio=request.POST["bio"],
    )
    if len(request.POST["snapchat"]):
        user.snapchat = request.POST["snapchat"]
    if len(request.POST["insta"]):
        print(request.POST["insta"])
        user.instagram = request.POST["insta"]
    if len(request.POST["othermedia"]):
        print(request.POST["othermedia"])
        user.other = request.POST["othermedia"]
    if len(request.POST["whatsapp"]):
        print(request.POST["whatsapp"])
        user.whatsapp = request.POST["whatsapp"]

    user.save()

    return redirect("profiles")
