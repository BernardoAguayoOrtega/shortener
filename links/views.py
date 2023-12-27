from django.shortcuts import render, get_object_or_404, redirect

from .models import Link

# Create your views here.


def index(request):
    links = Link.objects.all()
    
    context = {
        "links": links,
    }
    
    return render(request, "links/index.html", context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click() # This is the method we created in models.py
    return redirect(link.url) # This is the url field we created in models.py


def add_link(request):
   return render(request, "links/add_link.html")