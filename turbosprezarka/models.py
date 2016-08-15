from django.db import models

class TurboModel(models.Model):
      liczba_tlokow=models.IntegerField()
      cykl_pracy=models.CharField(max_length=3)
      objetosc_skokowa=models.FloatField()
      maksymalne_obroty_silnika=models.IntegerField()
      wspolczynnik_napelnienia=models.FloatField()
      moc_silnika=models.IntegerField()  
      sprawnosc_efektywna=models.IntegerField()       
# Create your models here.
