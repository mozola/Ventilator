from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import Parametry_wejscioweForm
from .model import Parametry_wejsciowe
import math
from django.shortcuts import redirect
from .model import Obliczenia_poczatkowe

def major(request):
    return render_to_response('major.html')


def parametry_poczatkowe_forms(request):
    if request.method == "POST":
       form=Parametry_wejscioweForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect(calculations)
    else:
        form=Parametry_wejscioweForm()
    return render(request,'parametry_wejsciowe_view.html',{'form':form})

def results(request):
     parametry=Parametry_wejsciowe.objects.all().last()
     return render(request,'przykladowe_obliczenia_view.html',{'uaop0':parametry})

def projects(request):
    return render_to_response("baseweb/projects.html")


def calculations(request):
    parametry=Parametry_wejsciowe.objects.all().last()

#przypisanie parametrow widoku do parametrow modelu    
    V_str_11=parametry.pierwszy_strumien_wydajnosci
    V_str_21=parametry.drugi_strumien_wydajnosci
    V_str_31=parametry.trzeci_strumien_wydajnosci
    dp_c1=parametry.przyrost_cisnienia_calkowitego
    p_01=parametry.cisnienie_otoczenia
    T_01=parametry.temperatura_otoczenia
    R=287


#obliczenia wstepne
    rho_01=(p_01)/(T_01 * R)
    v_str_01=(1.00)/(rho_01)
    m_str_1=(rho_01) * (V_str_21)

    K_n11=0.0351*pow((dp_c1/rho_01),(-0.75))*pow((V_str_21),(0.5))*parametry.n1
    K_n21=0.0351*pow((dp_c1/rho_01),(-0.75))*pow((V_str_21),(0.5))*parametry.n2
    K_n31=0.0351*pow((dp_c1/rho_01),(-0.75))*pow((V_str_21),(0.5))*parametry.n3
#pocztkowe wartosci delta   
    log_11=0.3364*pow((math.log(K_n11)),(2))-0.446*K_n11+0.1893
    log_21=(0.3364*(pow((math.log(K_n21)),(2))))-(0.446*(K_n21))+0.1893
    log_31=(0.3364*(pow((math.log(K_n31)),(2))))-(0.446*(K_n31))+0.1893
#zlogarytmizowane wartosci delta
    delta_11=math.log(log_11)
    delta_21=math.log(log_21)
    delta_31=math.log(log_31)
#srednice wirnika dla roznych predkosci obrotowych
    d_211=delta_11/6.783
    d_221=delta_21/6.783
    d_231=delta_31/6.783
#predkosc obwodowa wirnika
    u21=(3.14*d_211*parametry.n1)/(60)
#szerokosc wirnika
    
#tworzenie nowego obiektu z obliczonymi wartosciami
    a=Obliczenia_poczatkowe(
		           gestosc_wlasciwa=rho_01,
			   objetosc_wlasciwa=v_str_01,
 			   strumien_masy=m_str_1,
			   wskaznik_szybkobierznosci_1=K_n11,
                           wskaznik_szybkobierznosci_2=K_n21,
                           wskaznik_szybkobierznosci_3=K_n31,
                           wskaznik_srednicy_1=delta_11,
                           wskaznik_srednicy_2=delta_21,
                           wskaznik_srednicy_3=delta_31,
                           srednica_wirnika_1=d_211,
                           srednica_wirnika_2=d_221,
			   srednica_wirnika_3=d_231,
			   predkosc_obwodowa_wirnika=u21,
                           szerokosc_wirnika=1,
                           #skladowa_obwodowa_predkosci=1,

                           przekroj_wylotowy_wirnika=1,
                
                           skladowa_obwodowa_predkosci=1,
                          # przekroj_wylotowy_wirnika
           	           skladowa_promieniowa_predkosci=1, 

                           predkosc_wypadkowa=1,
                           predkosc_wzgledna=1,
                           katy_wyplywu_z_wirnika=1,
                           wskaznik_predkosci=1,
                           sredni_promien_na_wlocie_do_lopatki=1,
                           szerokosc_wirnika_na_wlocie=1,
                           przyspieszenie_przeplywu_na_wlocie=1,
                           pole_przekroju_wlotowego=1,
                           srednica_na_wlocie=1, 
                           predkosc_obwodowa=1,
                           kat_naplywu=1
                          )
    a.save()
    obliczenia_poczatkowe=Obliczenia_poczatkowe.objects.all().last()
    return render( request,'przykladowe_obliczenia_view.html',{'parametry':obliczenia_poczatkowe})





    
