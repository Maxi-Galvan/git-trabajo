from django.shortcuts import render

# Create your views here.
def read_anime(request):
    return render(request, 'TopAnime/TopAnimeIndex.html')


