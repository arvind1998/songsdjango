from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album



def index(request):
	all_albums=Album.objects.all()
	
	return render(request, 'music/index.html', {'var_album':all_albums})

def detail(request, album_id):
	try:
		album=Album.objects.get(pk=album_id)
		return render(request, 'music/detail.html',{'album':album,})

	except Album.DoesNotExist:
		raise Http404("Error 404: Album does not exist.")
	
