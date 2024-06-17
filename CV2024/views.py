import django
from django.http import request
from django.shortcuts import render, get_object_or_404
from webpack_loader.loader import WebpackLoader

class ExternalWebpackLoader(WebpackLoader):
    def load_assets(self):
        url = self.config['STATS_URL']
        return requests.get(url).json()

def index(request):

    name = "Marvin Uriel Largaespada Gonzalez"
    about = "Acerca de mi"
    
    return render(request, "pagina_1.html", {
        "name": name, "about" : about
    })

def page2(request):
    
    return render(request, "pagina_2.html")