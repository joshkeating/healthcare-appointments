from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):

	if request.method == 'POST':

        return
    else:
        return



def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
            
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

            # auth and login user
			user = authenticate(username=username, password=password)
            login(request, user)
			
			# redirect here
	else:
		# return the form if no input
		form = UserCreationForm()
	
