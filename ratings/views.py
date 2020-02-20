from django.shortcuts import render,redirect
from .forms import UserReagisterForm,PostUpdateForm
from django.contrib import messages
from .models import Project
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    projects = Project.objects.all()
    
    
    return render(request,"index.html",{"projects":projects})


def register(request):
    form=UserReagisterForm()
    if request.method == "POST":
        form=UserReagisterForm(request.POST)
        if form.is_valid():
                
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, ("Account for {} has been created successfully").format(username))
            return redirect("login")
    else:
        form=UserReagisterForm()
    return render(request, "register.html",{"form":form})
    
@login_required()
def submit(request):
    
    if request.method == "POST":
        form=PostUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=PostUpdateForm
  
    return render(request,"submit.html",{"form":form})

def profile(request):
    return render(request,"profile.html")

