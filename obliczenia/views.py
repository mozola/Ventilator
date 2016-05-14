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
    kappa=1.4
    Cp=1005

#obliczenia wstepne
    rho_01=(p_01)/(T_01*R)
    v_str_01=1/round(rho_01,2)
    m_str_1=(round(rho_01,2))*(round(V_str_21,2))
    K_n11=0.0351*(math.pow((dp_c1/rho_01),(-0.75)))*(math.pow((V_str_21),(0.5)))*parametry.n1
    K_n21=0.0351*math.pow((dp_c1/rho_01),(-0.75))*math.pow((V_str_21),(0.5))*parametry.n2
    K_n31=0.0351*pow((dp_c1/rho_01),(-0.75))*pow((V_str_21),(0.5))*parametry.n3
    

#pocztkowe wartosci delta   
    log_11=(0.3364*(math.pow((math.log10(round(K_n11,2))),(2))))-(0.446*math.log10(round(K_n11,2)))+0.1893
    log_21=(0.3364*(math.pow((math.log10(round(K_n21,3))),(2))))-(0.446*math.log10(round(K_n21,3)))+0.1893
    log_31=(0.3364*(math.pow((math.log10(round(K_n31,3))),(2))))-(0.446*math.log10(round(K_n31,3)))+0.1893

    print math.log10(K_n11)
#zlogarytmizowane wartosci delta
    delta_11=math.pow(10,(log_11))
    delta_21=math.pow(10,log_21)
    delta_31=math.pow(10,log_31)

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
    if K_n11 >= 0.04 and K_n11 < 0.06:
            b2_d2=0.0055
            b21=b2_d2*(d_211*1000)
            Psi_p1=1.8
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.2
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=71
    elif K_n11 >= 0.06 and K_n11 < 0.08:  
            b2_d2=0.015
            b21=b2_d2*(d_211*1000)
            Psi_p1=1.7
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.28
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=73

    elif K_n11 >= 0.08 and K_n11<0.10:
 	    b2_d2=0.025
            b21=b2_d2*(d_211*1000)
            Psi_p1=1.62
            C_2u1=(Psi_p1*u_21)/(2)
            r1_r2_1=0.33
            r_11=(r1_r2_1)*(d_211/2)
            eta_sw1=0.75

    elif K_n11 >= 0.10 and K_n11<0.15:
        b2_d2=0.036
        b21=b2_d2*(d_211*1000)
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

    elif K_n11 >= 0.15 and K_n11<0.20:
        b2_d2=0.057
        b21=b2_d2*(d_211*1000)
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

    elif K_n11 >= 0.20 and K_n11<0.25:
        b2_d2=0.069
        b21=b2_d2*(d_211*1000)
        Psi_p1=1.3
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.57
        r_11=(r1_r2_1)*(d_211/2)

    elif K_n11 >= 0.25 and K_n11 < 0.30:
        b2_d2=0.079
        b21=(b2_d2)*(d_211*1000)
        Psi_p1=1.25
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.6
        r_11=(r1_r2_1)*((d_211*1000)/2)
        eta_sw1=92
        delta_eta_pa=0.02
        delta_eta_sb=0.01
        eta_s=0.85
       
    elif K_n11 >= 0.30 and K_n11 < 0.40:
        b2_d2=0.088
        b21=b2_d2*(d_211*1000)
        Psi_p1=1.1
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.68
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=88

    elif K_n11 >= 0.40 and K_n11 < 0.50:
        b2_d2=0.105
        b21=b2_d2*(d_211*1000)
        Psi_p1=0.95
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.65
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=87

    elif K_n11 >= 0.50 and K_n11< 0.60:
        b2_d2=0.142
        b21=b2_d2*(d_211*1000)
        Psi_p1=0.83
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.8
        r_11=(r1_r2_1)*(d_211/2)

    elif K_n11 >= 0.60 and K_n11 < 0.70:
        b2_d2=0.177
        b21=b2_d2*(d_211*1000)
        Psi_p1=0.65
        C_2u1=(Psi_2*u_21)/(2)
        r1_r2_1=0.85
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=87

    elif K_n11 >= 0.70 and K_n11 < 0.80:
        b2_d2=0.186
        b21=b2_d2*(d_211*1000)
        Psi_p1=0.75
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2_1=0.88
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=0

    elif K_n11==0.80:
        b2_d2=0.229
        b21=b2_d2*(d_211*1000)
        Psi_p1=0
        C_2u1=(Psi_p1*u_21)/(2)
        r1_r2=0.91
        r_11=(r1_r2_1)*(d_211/2)
        eta_sw1=0

#przekroj wylotowy wirnika
    A_21=3.14*d_211*(b21*0.001)
#skladowa promieniowa predkosci
    C_2r1=V_str_21/A_21
#predkosc wypadkowa
    C_21=math.sqrt(math.pow((C_2r1),(2))+math.pow((C_2u1),(2)))
#predkosc wzgledna
    w_21=math.sqrt(math.pow((u_21-C_2u1),(2))+(math.pow(C_2r1,2)))
#katy wyplywu z wirnika
    beta_21=math.atan(math.tan((C_2r1)/(u_21-C_2u1)))
    alpha_21=math.atan(math.tan((C_2r1)/(C_2u1)))
#wskaznik predkosci
    fi_2r=(C_2r1)/(u_21)
#szerokosc wirnika na wlocie
    b_11=(b21)*(((d_211*1000)/(2))/(r_11))
#przyspieszenie przeplywu od przekroju 0-0 do przekroju 1-1
    c_01=(C_2r1)/(1.1)
#pole rzekroju 0-0
    A_01=2*3.14*(r_11*0.001)*(b_11*0.001)*(C_2r1/c_01)
#srednica d0
    d_01=(math.sqrt((4*A_01)/(3.14)))*1000
#predkosc obwodowa w przekroju 1-1
    u_11=(3.14*(r_11*2*0.001)*parametry.n1)/(60)
#kat naplywu w przekroju 1-1
    beta_11=math.atan((math.tan(C_2r1/u_11)))

#izentropowy przyrost entalpii (do tego momentu parametry zgadzaja sie z modelem wynikowym)
    delta_is_0_2_1=((eta_sw1*0.01)*(round(u_21,2))*(C_2u1))-((0.5)*(math.pow(C_21,2)-math.pow(c_01,2)))

#cisnienie na wlocie (zdefiniuj cp dla danego gazu)
    p_21=p_01*(math.pow(((delta_is_0_2_1/(Cp*T_01))+1),((kappa)/(kappa-1))))
    d_p02=p_21-p_01
#praca techniczna izentropowa
    l_ts_0_2c1=(delta_is_0_2_1)+((0.5)*(math.pow(C_21,2)-math.pow(c_01,2)))
#strata wystepujaca podczas przeplywu przez wirnik
    h_strat1=(u_21*C_2u1)-(l_ts_0_2c1)
#spadek sprawnosci w wirniku
    delta_eta_w1=(h_strat1)/(u_21*C_2u1)
#przyrost entalpii
    delta_i_0_2_1=(u_21*C_2u1)-(0.5)*(math.pow(C_21,2)-math.pow(c_01,2))
#przyrost temperatury
    T_21=(delta_i_0_2_1/Cp) + T_01
#gestosc powietrza za wirnikiem
    rho_21=(p_21)/(R*T_21)
#strumien objetosci
    V_str_21=m_str_1/rho_21
#sprawnosc_termodynaiczna_wirnika
    eta_s_0_1=(delta_is_0_2_1)/(delta_i_0_2_1)*100
    p_t1=p_21-p_01
#izentropowy wskaznik dla stopnia od ssania do tloczenia
    p_s1=p_21-d_p02
    peta=p_t1/p_s1
    peta=peta+1
    delta_i_sc1=(Cp*T_01)*((math.pow(peta,0.2857))-1)
#wskaznik pracy
    psi_sc1=(delta_i_sc1)/(0.5*(math.pow(u_21,2)))    
    psi_p1=(psi_sc1)/(eta_s*(1 + delta_eta_pa + delta_eta_sb))
#promien_r2pi
    B=0.120
    nr2pi=(V_str_21)/((d_211/2)*C_2u1*B)
    r_2pi_1=(d_211/2)*math.pow(math.e , nr2pi)
    h_1=(r_2pi_1*1000)-((d_211*1000)/2)
#Srednia_predkosc_wyplywu
    A_2pi1=(h_1*0.001)*B
    C_sr_1=V_str_21/A_2pi1
#Straty w kolektorze
     
#tworzenie nowego obiektu z obliczonymi wartosciami   
    a=Obliczenia_poczatkowe(
		           gestosc_wlasciwa=round(rho_01,2),
			   objetosc_wlasciwa=round(v_str_01,2),
 			   strumien_masy=round(m_str_1,2),
			   wskaznik_szybkobierznosci_1=round(K_n11,2),
                           wskaznik_szybkobierznosci_2=round(K_n21,3),
                           wskaznik_szybkobierznosci_3=round(K_n31,3),
                           wskaznik_srednicy_1=round(delta_11,2),
                           wskaznik_srednicy_2=round(delta_21,2),
                           wskaznik_srednicy_3=round(delta_31,2),
                           srednica_wirnika_1=round(d_211,2),
                           srednica_wirnika_2=round(d_221,2),
			   srednica_wirnika_3=round(d_231,2),
			   predkosc_obwodowa_wirnika=round(u_21,1),
                           szerokosc_wirnika=round(b21,2),
                           skladowa_obwodowa_predkosci=round(C_2u1,2),
                           przekroj_wylotowy_wirnika=round(A_21,3),    
           	           skladowa_promieniowa_predkosci=round(C_2r1,1), 
                           predkosc_wypadkowa=round(C_21,1),
                           predkosc_wzgledna=round(w_21,1),
                           katy_wyplywu_z_wirnika_beta_1=round(beta_21,1),
                           katy_wyplywu_z_wirnika_alpha_1=round(alpha_21,1),
                           wskaznik_predkosci=round(fi_2r,3),
                           sredni_promien_na_wlocie_do_lopatki=round(r_11,0),
                           szerokosc_wirnika_na_wlocie=round(b_11,0),
                           przyspieszenie_przeplywu_na_wlocie=round(c_01,1),
                           pole_przekroju_wlotowego=round(A_01,4),
                           srednica_na_wlocie=round(d_01,1), 
                           predkosc_obwodowa=round(u_11,1),
                           kat_naplywu=round(beta_11,1),
                           izentropowy_przyrost_entalpii= round(delta_is_0_2_1,2),
                           cisnienie_na_wylocie=round(p_21,2),
                           praca_techniczna_izentropowa=round(l_ts_0_2c1,2),
                           strata_wystepujaca_podczas_przeplywu_przez_wirnik=round(h_strat1,2),
                           spadek_sprawosci_w_wirniku=round(delta_eta_w1,0),
                           przyrost_entalpii_pomiedzy_przekrojem_0_0_a_2_2=round(delta_i_0_2_1,0),
                           temperatura_za_wirnikiem=round(T_21,0),
                           gestosc_powietrza_za_wirnikiem=round(rho_21,2),
                           strumien_objetosci_za_wirnikiem=round(V_str_21,3),
                           sprawnosc_termodynamiczna_wirnika=round(eta_s_0_1,0),
                           izentropowy_przyrost_entalpii_dla_stopnia_od_ssania_do_tloczenia=round(delta_i_sc1,1),
                           wskaznik_pracy=round(psi_p1,2),
                           promien_r2pi=round(r_2pi_1,3),
                           wysokosc_h=round(h_1,3),
                           przekroj_wylotowy_kolektora=round(A_2pi1,4),
                           srednia_predkosc_na_wylocie=round(C_sr_1,1),
                          )
    a.save()
    obliczenia_poczatkowe=Obliczenia_poczatkowe.objects.all().last()
    return render( request,'przykladowe_obliczenia_view.html',{'parametry':obliczenia_poczatkowe})




	
    
