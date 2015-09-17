from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.models import MyUser

# Create your views here.

class Home(TemplateView):
	template_name = 'home.html' 

	def get_context_data(self, **kwargs):
		context = super(Home,self).get_context_data(**kwargs)
		context['all'] = MyUser.objects.all()
		return context