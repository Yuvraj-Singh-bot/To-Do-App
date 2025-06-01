from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ToDoApplication import models
from .models import ToDoApp 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



# Create your views here.


#SignUp funtion 
def signup(request) : 
    if request.method == "POST" : 
        fnm = request.POST.get('fnm') 
        emailid = request.POST.get('emailid') 
        pwd = request.POST.get('pwd') 
        print(fnm,emailid,pwd) 
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/login') 
    

    
    return render(request, 'signup.html')


#Login Function 
def loginFunction(request) : 
    if request.method == 'POST' : 
        fnm = request.POST.get('fnm') 
        pwd = request.POST.get('pwd') 
        print(fnm,pwd) 
        userLog = authenticate(request,username = fnm,password = pwd) 
        
        if userLog is not None : 
            login(request,userLog)
            return redirect('/todopage') 
        else : 
            return redirect('/login') 
        
    return render(request,'login.html') 
 
#This is a Todo Function 
@login_required(login_url='/login')
def todo(request): 
    if request.method == 'POST': 
        title = request.POST.get('title') 
        print(title) 
        obj = models.ToDoApp(title=title, user=request.user) 
        obj.save() 
    
    all = models.ToDoApp.objects.filter(user=request.user).order_by('-date') 
    context = {'all': all}
    return render(request, 'todo.html', context) 


#This is the Delete Todo Function 
def delete_todo(request,srno) : 
    print(srno) 
    obj = models.ToDoApp.objects.get(srno=srno) 
    obj.delete() 
    return redirect('/todopage') 


#This is a ToDo SignOUt Function 
def signout(request) : 
    logout(request) 
    return redirect('/login') 

 
        
        

        


