from django import forms

class BlogForm(forms.Form):
	title = forms.CharField(label='Title:', max_length = 50000 )
	blog = forms.CharField(label='Post', max_length=50000, widget=forms.Textarea)

class UserForm(forms.Form):
	username = forms.CharField(label ='Username', max_length = 20)
	email = forms.EmailField(label ='E-Mail', max_length =100)
	password = forms.CharField(label='Password', max_length= 20, min_length=8, widget=forms.PasswordInput)

class LoginForm(forms.Form):
	username = forms.CharField(label ='Username', max_length = 20)
	password = forms.CharField(label='Password', max_length= 20, min_length=8, widget=forms.PasswordInput)
