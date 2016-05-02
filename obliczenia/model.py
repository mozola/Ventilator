from django.db import models

class Parametry_wejsciowe(models.Model):
    pierwszy_strumien_wydajnosci=models.FloatField(max_length=5) 
    drugi_strumien_wydajnosci=models.FloatField(max_length=5)    
    trzeci_strumien_wydajnosci=models.FloatField(max_length=5)        
    przyrost_cisnienia_calkowitego=models.FloatField(max_length=5)
    cisnienie_otoczenia=models.FloatField(max_length=5)
    temperatura_otoczenia=models.FloatField(max_length=5) 
  #  sprezany_czynnik=models.FloatField(max_length=10,choice=czynniki)
    cieplo_parowania=models.FloatField(max_length=5) 
    n1=models.IntegerField(max_length=5)
    n2=models.IntegerField(max_length=5)
    n3=models.IntegerField(max_length=5)
       

class Obliczenia_poczatkowe(models.Model):
    gestosc_wlasciwa=models.FloatField(max_length=5)
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
    katy_wyplywu_z_wirnika=models.FloatField(max_length=5)
    wskaznik_predkosci=models.FloatField(max_length=5)
    sredni_promien_na_wlocie_do_lopatki=models.FloatField(max_length=5)
    szerokosc_wirnika_na_wlocie=models.FloatField(max_length=5)
    przyspieszenie_przeplywu_na_wlocie=models.FloatField(max_length=5)
    pole_przekroju_wlotowego=models.FloatField(max_length=5)
    srednica_na_wlocie=models.FloatField(max_length=5)
    predkosc_obwodowa=models.FloatField(max_length=5)
    kat_naplywu=models.FloatField(max_length=5)

    

