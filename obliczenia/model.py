from django.db import models
from django.utils.timezone import now as timezone_now
import os
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch


class Parametry_wejsciowe(models.Model):
    pierwszy_strumien_wydajnosci=models.FloatField("strumien wydajnosci 1 (m^3/s):",max_length=5) 
    drugi_strumien_wydajnosci=models.FloatField("strumien wydajnosci 2 (m^3/s):",max_length=5)    
    trzeci_strumien_wydajnosci=models.FloatField("strumien wydajnosci 3 (m^3/s):",max_length=5)        
    przyrost_cisnienia_calkowitego=models.FloatField("Przyrost cisnienia calkowitego (Pa):",max_length=5)
    cisnienie_otoczenia=models.FloatField("Cisnienie otoczenia (Pa):",max_length=5)
    temperatura_otoczenia=models.FloatField("Temperatura otoczenia (K):",max_length=5) 
  #  sprezany_czynnik=models.FloatField(max_length=10,choice=czynniki)
  #  cieplo_parowania(J/kg)=models.FloatField(max_length=5) 
    n1=models.IntegerField("n1 (obr/min):",max_length=5)
    n2=models.IntegerField("n2 (obr/min)",max_length=5)
    n3=models.IntegerField("n3 (obr/min)",max_length=5)
       

class Obliczenia_poczatkowe(models.Model):
    gestosc_wlasciwa=models.FloatField(max_length=10)
    objetosc_wlasciwa=models.FloatField(max_length=5)
    strumien_masy=models.FloatField(max_length=5)
    wskaznik_szybkobierznosci_1=models.FloatField(max_length=5)
    wskaznik_szybkobierznosci_2=models.FloatField(max_length=5)
    wskaznik_szybkobierznosci_3=models.FloatField(max_length=5) 

    wskaznik_srednicy_1=models.FloatField(max_length=5)
    wskaznik_srednicy_2=models.FloatField(max_length=5)
    wskaznik_srednicy_3=models.FloatField(max_length=5)

    srednica_wirnika_1=models.FloatField(max_length=5)
    srednica_wirnika_2=models.FloatField(max_length=5)
    srednica_wirnika_3=models.FloatField(max_length=5)

    predkosc_obwodowa_wirnika=models.FloatField(max_length=5)
    szerokosc_wirnika=models.FloatField(max_length=5)
    #skladowa_obwodowa_predkosci=models.FloatField(max_length=5)
    przekroj_wylotowy_wirnika=models.FloatField(max_length=5)
    skladowa_obwodowa_predkosci=models.FloatField(max_length=5)
   # przekroj_wylotowy_wirnika=models.FloatField(max_length=5)
    skladowa_promieniowa_predkosci=models.FloatField(max_length=5)
    predkosc_wypadkowa=models.FloatField(max_length=5)
    predkosc_wzgledna=models.FloatField(max_length=5)
    katy_wyplywu_z_wirnika_alpha_1=models.FloatField(max_length=5)
    katy_wyplywu_z_wirnika_beta_1=models.FloatField(max_length=5)
    wskaznik_predkosci=models.FloatField(max_length=5)
    sredni_promien_na_wlocie_do_lopatki=models.FloatField(max_length=5)
    szerokosc_wirnika_na_wlocie=models.FloatField(max_length=5)
    przyspieszenie_przeplywu_na_wlocie=models.FloatField(max_length=5)
    pole_przekroju_wlotowego=models.FloatField(max_length=5)
    srednica_na_wlocie=models.FloatField(max_length=5)
    predkosc_obwodowa=models.FloatField(max_length=5)
    kat_naplywu=models.FloatField(max_length=5)    
    izentropowy_przyrost_entalpii=models.FloatField(max_length=5)
    cisnienie_na_wylocie=models.FloatField(max_length=5)
    praca_techniczna_izentropowa=models.FloatField(max_length=5)
    strata_wystepujaca_podczas_przeplywu_przez_wirnik=models.FloatField(max_length=5)
    spadek_sprawosci_w_wirniku=models.FloatField(max_length=5)
    przyrost_entalpii_pomiedzy_przekrojem_0_0_a_2_2=models.FloatField(max_length=5)
    temperatura_za_wirnikiem=models.FloatField(max_length=5)
    gestosc_powietrza_za_wirnikiem=models.FloatField(max_length=5)
    strumien_objetosci_za_wirnikiem=models.FloatField(max_length=5)
    sprawnosc_termodynamiczna_wirnika=models.FloatField(max_length=5)
    izentropowy_przyrost_entalpii_dla_stopnia_od_ssania_do_tloczenia=models.FloatField(max_length=5)
    wskaznik_pracy=models.FloatField(max_length=5)
    promien_r2pi=models.FloatField(max_length=5)
    wysokosc_h=models.FloatField(max_length=5)
    przekroj_wylotowy_kolektora=models.FloatField(max_length=5)
    srednia_predkosc_na_wylocie=models.FloatField(max_length=5)    


class Aktualnosci(models.Model):
    tytul=models.CharField(max_length=70)
    tekst=models.TextField()
    autor=models.CharField(max_length=70)

def upload_to(instance,filename):
    now=timezone_now()
    filename_base, filename_ext=os.path.splitext(filename)
    return 'producrs/%s/%s%s' % (
       instance.product.slug,
       now.strftime("%Y%m%d%H%M%S"),
       filename_ext.lower(),
    )

class Realizowane_projekty(models.Model):
     tytul_projektu=models.CharField(max_length=100)
     opis=models.TextField()
     zdjecie_projektu=models.ImageField(upload_to='temps/', default='temps/no_img.jpg')
