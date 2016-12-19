from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .models import users
from .forms import ContactForm

def index(request):
    return render(request, 'maildir/index.html')
	

def list(request):
	user_objects = users.objects.all().order_by('-id')
	context = {'users': user_objects}
	return render(request, 'maildir/list.html', context)
	
	
def create(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			context = {
				'fname': user.first_name,
				'lname': user.last_name,
				'email': user.email
			}
			return redirect('/list', context)
	else:
		form = ContactForm()
	return render(request, 'maildir/add.html', {'form': form})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
