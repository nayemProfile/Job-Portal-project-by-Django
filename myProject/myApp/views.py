from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import login,logout,authenticate
from myApp.models import *
from myProject.forms import *

# Create your views here.

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
    else:
        form=customUserForm()


    return render(request,"signup.html",{'form':form})   
    


def loginPage(request):
    if request.method == 'POST':
        form=customUserAutenticationForm(request,data=request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(request,username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect("dashboard")
            else:
                return HttpResponse("Username or Password did not match")
    else:
            form=customUserAutenticationForm()

    return render(request,"login.html",{'form':form})

def logoutPage(request):
    logout(request)
    return redirect("loginPage")


def dashboard(request):
    return render(request,'dashboard.html')

def viewjobPage(request):
    job=JobModel.objects.all()
    if request.method == "POST":
        form=jobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewjobPage")
    else:
        form=jobForm()
   
    return render(request,'viewjobPage.html',{'job':job,'form':form})



def jobAdd(request):
    if request.method == "POST":
        form=jobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewjobPage")
    else:
        form=jobForm()
    return render(request,'viewjobPage.html', {'form':form})
        
def deletejob(request,id):
    job=JobModel.objects.get(id=id)
    job.delete()
    return redirect("viewjobPage")

def editjob(request,id):
    job=JobModel.objects.get(id=id)
    form=jobForm(instance=job)
    if request.method == "POST":
        form=jobForm(request.POST,instance=job)
        
        form.save()
        return redirect("viewjobPage")
    
    return render(request,"editjob.html",{'form':form})



def search(request):
    try:
        query = request.GET.get("q")
        if query:
            jobs = JobModel.objects.filter(job_position__icontains = query)
        else:
            jobs = [] 
        context = {
            "quary":query,
            "jobs": jobs,
        }
        return render(request, 'search.html', context)
    except Exception as e:
        return HttpResponse("Exception error", {{e}})