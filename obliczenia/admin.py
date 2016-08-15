from django.contrib import admin
from .model import Parametry_wejsciowe
from .model import Obliczenia_poczatkowe
from .model import Aktualnosci
from .model import Realizowane_projekty
#from .models import TurboModel

admin.site.register(Parametry_wejsciowe)
admin.site.register(Obliczenia_poczatkowe)
admin.site.register(Aktualnosci)
admin.site.register(Realizowane_projekty)
#admin.site.register(TurboModel)                
