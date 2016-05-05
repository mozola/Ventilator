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
    p_01=p_01*100000
    kappa=1.4
    Cp=1005

#obliczenia wstepne
    rho_01=(p_01)/(T_01*R)
    v_str_01=1/rho_01
    m_str_1=(rho_01) * (V_str_21)
    print p_01
    print T_01
    print R
    print dp_c1
    print v_str_01
    print rho_01
    print math.pow(4,1/2)
    print math.pow((dp_c1/rho_01),(-0.75))

    K_n11=0.0351*(math.pow((dp_c1/rho_01),(-0.75)))*(math.pow((V_str_21),(0.5)))*parametry.n1
    K_n21=0.0351*math.pow((dp_c1/rho_01),(-0.75))*math.pow((V_str_21),(0.5))*parametry.n2
    K_n31=0.0351*pow((dp_c1/rho_01),(-0.75))*pow((V_str_21),(0.5))*parametry.n3
    

    print K_n11
    print K_n21
    print K_n31

#pocztkowe wartosci delta   
    log_11=0.3364*(math.pow((math.log10(K_n11)),(2)))-(0.446*(K_n11))+0.1893
    log_21=0.3364*(math.pow((math.log10(K_n21)),(2)))-(0.446*(K_n21))+0.1893
    log_31=0.3364*(math.pow((math.log10(K_n31)),(2)))-(0.446*(K_n31))+0.1893

    print math.log10(K_n11)
#zlogarytmizowane wartosci delta
    delta_11=3.67 #math.pow(10,(log_11))
    delta_21=7.9 #math.pow(10,log_21)
    delta_31=16.2 #math.pow(10,log_31)

    print delta_11
    print delta_21
    print delta_31   
 
#srednice wirnika dla roznych predkosci obrotowych
    d_211=delta_11/6.783
    d_221=delta_21/6.783
    d_231=delta_31/6.783
#predkosc obwodowa wirnika
    u_21=(3.14*d_211*parametry.n1)/(60)
#szerokosc wirnika
    if K_n11 >= 0.04 or K_n11 < 0.06:
            b2_d2=0.0055
            b21=b2_d2*d_211
            Psi_p1=1.8
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.2
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=71
    elif K_n11 >= 0.06 or K_n11 < 0.08:  
            b2_d2=0.015
            b21=b2_d2*d_211
            Psi_p1=1.7
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.28
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=73

    elif K_n11 >= 0.08 or K_n11<0.10:
 	    b2_d2=0.025
            b21=b2_d2*d_211
            Psi_p1=1.62
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.33
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=0.75

    elif K_n11 >= 0.10 or K_n11<0.15:
        b2_d2=0.036
        b21=b2_d2*d_211
        Psi_p1=1.5
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.42
        r_11=(r1_r2_1)*(d_211/2)
        if K_n11==10:
           eta_sw1=80
        elif K_n11==0.11:
           eta_sw1=81
        elif K_n11==0.12:
           eta_sw1= 82
        elif K_n11==0.13:
           eta_sw1=83
        elif K_n11==0.14:
           eta_sw11=84

    elif K_n11 >= 0.15 or K_n11<0.20:
        b2_d2=0.057
        b21=b2_d2*d_211
        Psi_p1=1.45
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.5
        r_11=(r1_r2_1)*(d_211/2)
        if K_n11==0.15:
           eta_sw1=85
        elif K_n11==0.16:
           eta_sw1=86
        elif K_n11==0.17:
           eta_sw1=87
        elif K_n11==0.18:
           eta_sw1=88
        elif K_n11==0.19:
           eta_sw1=89

    elif K_n11 >= 0.20 or K_n11<0.25:
        b2_d2=0.069
        b21=b2_d2*d_211
        Psi_p1=1.3
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.57
        r_11=(r1_r2_1)*(d_211/2)

    elif K_n11 >= 0.25 or K_n11 < 0.30:
        b2_d2=0.079
        b21=b2_d2*d_211
        Psi_p1=1.25
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.6
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=92
       
    elif K_n11 >= 0.30 or K_n11 < 0.40:
        b2_d2=0.088
        b21=b2_d2*d_211
        Psi_p1=1.1
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.68
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=88

    elif K_n11 >= 0.40 or K_n11 < 0.50:
        b2_d2=0.105
        b21=b2_d2*d_211
        Psi_p1=0.95
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.65
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=87

    elif K_n11 >= 0.50 or K_n11< 0.60:
        b2_d2=0.142
        b21=b2_d2*d_211
        Psi_p1=0.83
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.8
        r_11=(r1_r2_1)*(d_211/2)

    elif K_n11 >= 0.60 or K_n11 < 0.70:
        b2_d2=0.177
        b21=b2_d2*d_211
        Psi_p1=0.65
        C_2u1=(Psi_2*u_21)/(2)
        r1_r2_1=0.85
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=87

    elif K_n11 >= 0.70 or K_n11 < 0.80:
        b2_d2=0.186
        b21=b2_d2*d_211
        Psi_p1=0.75
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.88
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=0

    elif K_n11==0.80:
        b2_d2=0.229
        b21=b2_d2*d_211
        Psi_p1=0
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2=0.91
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=0

     
#przekroj wylotowy wirnika
    A_21=3.14*d_211*b21
#skladowa promieniowa predkosci
    C_2r1=V_str_21/A_21
    print V_str_21
#predkosc wypadkowa
    C_21=math.sqrt(math.pow((C_2r1),(2))+math.pow((C_2u1),(2)))
#predkosc wzgledna
    w_21=math.sqrt(math.pow((u_21-C_2u1),(2))+(math.pow(C_2r1,2)))
#katy wyplywu z wirnika
    beta_21=math.tan((u_21-C_2u1)/(C_2r1))
    alpha_21=math.tan((C_2u1)/(C_2r1))
#wskaznik predkosci
    fi_2r=(C_2r1)/(u_21)
#szerokosc wirnika na wlocie
    b_11=b21*((d_211)/r_11)
#przyspieszenie przeplywu od przekroju 0-0 do przekroju 1-1
    c_01=(C_2r1)/(1.1)
#pole rzekroju 0-0
    A_01=2*3.14*r_11*(C_2r1/c_01)
#srednica d0
    d_01=math.sqrt((4*A_01)/(3.14))
#predkosc obwodowa w przekroju 1-1
    u_11=(3.14*d_211*parametry.n1)/(60)
#kat naplywu w przekroju 1-1
    beta_11=math.tan(C_2r1/u_11)
#izentropowy przyrost entalpii (do tego momentu parametry zgadzaja sie z modelem wynikowym)
    delta_is_0_2_1=(eta_sw1*(1/2)*(math.pow(C_21,2)-math.pow(C_2r1,2)))
#cisnienie na wlocie (zdefiniuj cp dla danego gazu)
    p_21=p_01*math.pow(((delta_is_0_2_1/(Cp*T_01))+1),(kappa/(kappa-1)))
#praca techniczna izentropowa
    l_ts_0_2c1=delta_is_0_2_1+(1/2)*(math.pow(C_21,2)-math.pow(c_01,2))
#strata wystepujaca podczas przeplywu przez wirnik
    h_strat1=( u_21*C_2u1) - l_ts_0_2c1
#spadek sprawnosci w wirniku
    delta_eta_w1=(h_strat1)/(u_21*C_2u1)
#przyrost entalpii
    delta_i_0_2_1=((u_21*C_2u1)-(1/2)*(math.pow(C_21,2)-math.pow(c_01,2)))
#przyrost temperatury
    T_21=(delta_i_0_2_1/Cp) + T_01
#gestosc powietrza za wirnikiem
    rho_21=p_21/R*T_21
#strumien objetosci
    V_str_21=m_str_1/rho_21
#sprawnosc termodynamiczna wirnika
    eta_s_0_1=delta_is_0_2_1/delta_i_0_2_1
#promien r_2pi
    r_2pi_1=(d_211/2)*(math.pow(math.e,0.894))
#wysokosc h
    h_1=r_2pi_1-(d_211/2)
#parametr B
    B_1=120
#przekroj wylotowy z kolektora
    A_2pi_1=h_1*B_1
#Srednia_predkosc_wyplywu
    c_sr_1=V_str_21/A_2pi_1
#Straty w kolektorze

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
			   predkosc_obwodowa_wirnika=u_21,
                           szerokosc_wirnika=b21,
                           skladowa_obwodowa_predkosci=C_2u1,
                           przekroj_wylotowy_wirnika=A_21,    
           	           skladowa_promieniowa_predkosci=C_2r1, 
                           predkosc_wypadkowa=C_21,
                           predkosc_wzgledna=w_21,
                           katy_wyplywu_z_wirnika=beta_21,
                           wskaznik_predkosci=fi_2r,
                           sredni_promien_na_wlocie_do_lopatki=r_11,
                           szerokosc_wirnika_na_wlocie=b_11,
                           przyspieszenie_przeplywu_na_wlocie=c_01,
                           pole_przekroju_wlotowego=A_01,
                           srednica_na_wlocie=d_01, 
                           predkosc_obwodowa=u_11,
                           kat_naplywu=beta_11,
                           izentropowy_przyrost_entalpii= delta_is_0_2_1,
                           cisnienie_na_wylocie=p_21,
                           praca_techniczna_izentropowa=l_ts_0_2c1,
                           strata_wystepujaca_podczas_przeplywu_przez_wirnik= h_strat1,
                           spadek_sprawosci_w_wirniku=delta_eta_w1,
                           przyrost_entalpii_pomiedzy_przekrojem_0_0_a_2_2=delta_i_0_2_1,
                           temperatura_za_wirnikiem=T_21,
                           gestosc_powietrza_za_wirnikiem=rho_21,
                           strumien_objetosci_za_wirnikiem=V_str_21,
                           sprawnosc_termodynamiczna_wirnika=eta_s_0_1,
                           izentropowy_przyrost_entalpii_dla_stopnia_od_ssania_do_tloczenia=1,
                           wskaznik_pracy=1,
                           promien_r2pi=r_2pi_1,
                           wysokosc_h=h_1,
                           przekroj_wylotowy_kolektora=A_2pi_1,
                           srednia_predkosc_na_wylocie=c_sr_1,                          
                          )
    a.save()
    obliczenia_poczatkowe=Obliczenia_poczatkowe.objects.all().last()
    return render( request,'przykladowe_obliczenia_view.html',{'parametry':obliczenia_poczatkowe})





    
