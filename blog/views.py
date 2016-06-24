from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from blog.models import Blog
from .forms import BlogForm, UserForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    data = Blog.objects.all()
    return TemplateResponse(request,'blog/index.html',{"data": data})

@login_required 
def add(request):
	form = BlogForm()
	return render(request, 'blog/blog.html', {'form': form})

@login_required 
def post(request):
	form = BlogForm(request.POST)

	if form.is_valid():
		user = request.user
		author = user.get_username()
		title = form.cleaned_data['title']
		blog = form.cleaned_data['blog']
		post = Blog.objects.create(author=author,title=title, body = blog)

	return profile(request)

    
def error(request):
	return TemplateResponse(request,'blog/error.html',{})

def add_user(request):
	form = UserForm()
	return render(request,'blog/newuser.html',{'form':form})

def new_user(request):
	form = UserForm(request.POST)
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		user = User.objects.create_user(username,email,password)
	return TemplateResponse(request,'blog/usersucc.html',{})
	

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	print username
	print password
	user = authenticate(username=username, password=password)
	print "in views.login"
	
	if user is not None:
		print "inside the if"
		if user.is_active:
			login(request, user)
       		data = Blog.objects.all()
    		return TemplateResponse(request,'blog/index.html',{"data": data})
            # Redirect to a success page.
        else:
        	return TemplateResponse(request,'blog/error.html',{})
            # Return a 'disabled account' error message
	
	
	return TemplateResponse(request,'blog/error.html',{})
		

@login_required 
def profile(request):
	form = BlogForm()
	data = Blog.objects.all()
	return TemplateResponse(request,'blog/loggedin.html',{"data": data , "form": form})


@login_required
def filter(request):
	user = request.user
	name = user.get_username()
	data = Blog.objects.all().filter(author = name)
	form = BlogForm()
	return TemplateResponse(request,'blog/userview.html',{"data": data, "form": form})


