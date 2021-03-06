from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from blog.models import Blog
from comments.models import Comment
from .forms import BlogForm, UserForm, LoginForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    data = Blog.objects.all()
    comments = Comment.objects.all()
    return TemplateResponse(request,'blog/index2.html',{"data": data, "comments":comments})

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
	return TemplateResponse(request,'blog/error2.html',{})

def add_user(request):
	form = UserForm()
	return render(request,'blog/newuser2.html',{'form':form})

def new_user(request):
	form = UserForm(request.POST)
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		user = User.objects.create_user(username,email,password)
	return TemplateResponse(request,'blog/usersucc2.html',{"username": username})
	

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
	user = request.user
	username = user.get_username()
	form = BlogForm()
	data = Blog.objects.all()
	comments = Comment.objects.all()
	return TemplateResponse(request,'blog/loggedin2.html',{"data": data, "comments": comments , "form": form ,"username": username})


@login_required
def filter(request):
	user = request.user
	username = user.get_username()
	data = Blog.objects.all().filter(author = username)
	form = BlogForm()
	comments = Comment.objects.all()
	return TemplateResponse(request,'blog/userview2.html',{"data": data, "comments": comments, "username":username, "comment":comment})

def comment(request):
	form = CommentForm(request.POST)
	print "here"

	if form.is_valid() :
		print "hereeeee"
		post = form.cleaned_data['post']
		comment = form.cleaned_data['comment']
		blog_id = form.cleaned_data['blog_id']
		user = request.user
		username = user.get_username()
		newcomment = Comment.objects.create(post= post, comment= comment, username=username, blog_id=blog_id)

	return profile(request)





