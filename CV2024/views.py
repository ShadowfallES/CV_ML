import django
from django.http import request, HttpResponse
from django.shortcuts import render, get_object_or_404
from webpack_loader.loader import WebpackLoader
class ExternalWebpackLoader(WebpackLoader):
    def load_assets(self):
        url = self.config['STATS_URL']
        return requests.get(url).json()

def index(request):

    Indice_Pagina_1 = {
        "Acerca" : "Acerca de mí",
        "Educacion" : "Educación"
    }

    Datos_Pagina_1 = {
        "Nombre" : "Marvin Uriel Largaespada Gonzalez",
        "text_acerca" : """Tengo 25 años y actualmente estoy cursando el quinto año de Ingeniería en
                        Computación en la Universidad Nacional de Ingeniería. Me caracterizo por ser una
                        persona trabajadora y cumplidora, comprometido con mis estudios y metas
                        académicas.""",
        "Carrera" : "Ingeniería en Computación",
        "Universidad" : "Universidad Nacional de Ingeniería",
        "Curso_CS50" : "CS50: Introduction to Computer Science",
        "Entidad": "Fundación Uno",
        "Info_CS50" : """CS50 es un programa de Fundación Uno con la colaboración de la Universidad Nacional de Ingeniería UNI, basado en el curso CS50 de Harvard University.
        """
    }
    
    Reponse = render(request, "pagina_1.html", {"Indice_Pagina_1" : Indice_Pagina_1,"Datos" : Datos_Pagina_1})
    Reponse.status_code = 200

    return Reponse

def page2(request):
    
    Reponse = render(request, "pagina_2.html")
    Reponse.status_code = 200

    return Reponse 

def vista_404(request):
    return HttpResponse ("Pagina no existe", status = 404)