from django.shortcuts import render

# Create your views here.
def index(request)
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
    return render(request, "index.html",{"form":form})


def register(request):
    return render(request,"register.html")

def profile(request):
    return render(request,"profile.html")