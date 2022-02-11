from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Contact
from bloging.models import Post
from django.contrib.auth import login,logout,authenticate
# Create your views here.
# HTML Pages
def home (request):
    return render (request,'home/home.html' )



def contact (request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg=request.POST['content']
        if   len(phone)<11:
            messages.error(request,"Please Fill Form Correctly")

        else:
            contact=Contact(name=name,email=email,phone=phone,content=msg)
            contact.save()
            messages.success(request,"Your Form has been submit Sucessfully ")
    return render (request,'home/contact.html',context={'user':request.user})

def search(request):
    query=request.GET['query']
    # Here we are checking length of query
    if len(query) >60:
        post=Post.objects.none()
    else: 
        posttitle=Post.objects.filter(title__icontains=query)
        postcontent=Post.objects.filter(content__icontains=query)
        # Here we are merging 2 queries
        post=posttitle.union(postcontent)
        # post=Post.objects.filter(title__icontains=query)
    if post.count() ==0:
        messages.warning(request,"No Search Result Found Please Refine your Query")
    context={'post':post,'query':query}
    return render(request,'home/search.html',context)

#Authentication and APIs
# Signup 
def handlesignup(request):
    if request.method=='POST':
        # For geting Post Parameters
        username=request.POST['username']
        fname=request.POST['fname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # Here we are creating some validation in from
        if len(username)>10:
            messages.error(request,"Plsease Enter Correct Username. Username Length must be Under 10")
            return redirect('home')
        # Matching pass1 and pass2
        if pass1!=pass2:
            messages.error(request,"Your Password and Confrom Password do not Match")
            return redirect('home')
        # Only takes alpha numeric user name
        if not username.isalnum():
            messages.error(request,"Plsease Enter Correct Username. your Username should Contain Letters and Numbers")
            return redirect('home')

        

        # Create a User Here 
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'Your Account has been Created Successfully')
        return redirect('home')



    else:
        return HttpResponse('404 - Not Found ')

#  Login
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user =authenticate(username=loginusername,password=loginpass)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Sucessfully Logedin!! ")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials !! Please Try Again")
            return redirect('home')

        
    # return HttpResponse('404 - Not Found ')

# Logout
def handlelogout(request):
    
    logout(request)
    messages.error(request,"You Are Sucessfully Loged Out!!")
    return redirect('home')
    