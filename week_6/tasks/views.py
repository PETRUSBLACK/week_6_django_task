from django import forms
from django.forms.widgets import TextInput
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.auth import authenticate, login, logout


tasks = [ ]
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Here")
    # tasks_2 = forms.CharField(label="content")

def index(request):
    # if "tasks" not in request.session:
    #     request.session["tasks"] = [ ]
    return render(request, "tasks/index.html", {
        "tasks": tasks
        # "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


def login_view(request):
     if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=  password)
         if user is not None:
             login(request, user)
             return HttpResponseRedirect(reverse("tasks:index"))
         else:
             return render(request, "tasks/add.html", {
                 "message" : "Invalid"
             })
     return render(request, "tasks/login.html")



# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# # Create your views here.
# def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("login"))
    

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=  password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "users/login.html", {
#                 "message" : "Invalid"
#             })
#     return render(request, "users/login.html")

# def logout_view(request):
#     return render(request, "users/logout.html")

# def register_view(request):
#     return render(request, "users/register.html")