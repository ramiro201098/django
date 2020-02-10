from django.shortcuts import render

from django.http import HttpResponse

def post_list(request):
	print(request)
	return HttpResponse("<h1>Hola Mundo</h1>")

def first_view(request):
	return render(request,"base.html")
# Create your views here.
