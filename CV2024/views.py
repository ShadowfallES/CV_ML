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
    
    Indice_pagina_2 = {
        "Habilidades": "Habilidades",
        "Habilidades_Blandas": "Habilidades Blandas"
    }

    Datos_Pagina_2 = {
        "Curso_Web50" : "CS50’s Web Programming with Python and JavaScript",
        "IT" : "IT Essentials",
        "Linux" : "NGD Linux Unhatched",
        "Entidad_1" : "Fundación Uno",
        "Entidad_2" : "Centro Juvenil Don Bosco",
        "Web50" : """Profundizando más en el diseño y la implementación de aplicaciones web con Python, JavaScript y SQL utilizando marcos como Django y Bootstrap.""",
        "ITESSENTIAL" : "IT Essentials abarca los principios básicos de hardware y software informático.",
        "NGDLINUX" : "Curso básico de Linux es ofrecido por Network Development Group (NDG)."
        
    }

    Reponse = render(request, "pagina_2.html", {"Indice" : Indice_pagina_2, "Datos" : Datos_Pagina_2})
    Reponse.status_code = 200

    return Reponse 

def vista_404(request):
    return HttpResponse ("Pagina no existe", status = 404)