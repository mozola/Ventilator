from django.shortcuts import render
from .models import TurboModel
from .models import TurboResultModel
from .forms import TurboForm
from django.shortcuts import render_to_response
from django.shortcuts import redirect
import math

def TurboParametry(request):
     if request.method == 'POST':
        form=TurboForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect(TurboResult)
     else:
        form=TurboForm()
     return render(request,'TurboParametry.html',{'form':form})

#tutaj zaczynaja sie metody obliczeniowe#

def m_str(a,b,c,d):
     return ((a*b)/(120))*(c*d)
def l_iz(a,b,kappa):
     return((kappa)/(kappa-1))*287.05*a* (math.pow(b,((kappa-1)/(kappa)))-1)
def u2(a,b):
     return math.pow(((a)/(b)),0.5)
def T1(a,b,c):
    c1a=b*c
    return a-((math.pow(c1a,2))/(2*(1.4/(1.4-1)*287.05)))
def w1(Mw1,T1,kappa):
    return Mw1 * math.pow((kappa*287.05*T1),2) #naniesiona zmiana w potedze, powinno byc 0.5
def u1(a,D1D2):
    return ((a)*D1D2)
def p1(delta1,P0,T1,T0,kappa):
    return delta1*P0*math.pow((T1/T0),(kappa/(kappa-1)))
def beta1(c1,w1):
    return math.asin(c1/w1)
def mi(z,D1D2,D0D2):
    rsrr2=math.pow((math.pow(D1D2,2)-math.pow(D0D2,2))/(2),0.5)
    return (1)/(1+(2*3.14)/3131-math.pow(0.47,2))    
def c2u(mi,u2):
    return mi*u2
def c2(c2u,c2r):
    return math.pow((math.pow(c2u,2)+math.pow(c2r,2)),0.5)
def w2(u2,c2u,c2r):
    return math.pow((math.pow((u2-c2u),2)+math.pow(c2r,2)),0.5)
def beta2(c2r,w2):
    kat=c2r/w2
    return math.acos(kat)
def T2(T1,mi,alpha,u2,kappa):
    return T1+(mi+alpha-(math.pow(mi,2)/2))*(math.pow(u2,2)/(kappa*287.05/kappa-1))
def p2(p1,T2,T1,n):
    return p1*math.pow((T2/T1),(n/(n-1)))
def A1(mstr,T1,C1a,p1):
    return (mstr*T1*287.05)/(c1a*p1)
def D2(A1,D1D2,D0D2):
    return math.pow(((4*A1)/(3.14*(math.pow(D1D2,2)-math.pow(D0D2,2)))),0.5)
def D1(D2,D1D2):
    return D2*(D1D2)
def D0(D2,D0D2):
    return D2*D0D2
def b(mstr,D2,C2rA,p2,T2):
    return (mstr)/(3.14*D2*C2r*(P2/(287.05*T2)))
def h1(D2):
    return 0.23*D2
def rp(D2):
    return 0.43*D2
def D2_kr(D2,s):
    return D2+(2*s)
def C2_kr(C2,D2,D2_kr):
    return C2*(D2/D2_kr)
def T2_kr(T2,C2,kappa,C2_kr):
    return T2+((math.pow(c2,2)-math.pow(c2_kr,2))/(2*(kappa/(kappa-1)*287.05)))
def p2_kr(p2,T2_kr,T2,n):
    return P2*math.pow((T2_kr/T2),(n/(n-1)))
def T3(T3_kr,c3,kappa,c2_kr):
    T3_kr=T2_kr+((math.pow(c2_kr,2))/(2 *287.05*(kappa/(kappa-1))))
    return T3_kr+((math.pow(c3,2))/(2*287.05*(kappa/(kappa-1))))
def p3(p2_kr,T3,T2_kr,n):
    return T2_kr*math.pow((T3)/(T2_kr),(n/(n-1)))
def A3(mstr,T3,c3,p3):
    return (mstr*T3*287.05)/(c3*p3)
def n(u2,D2):
    return (60*u2)/(3.14*D2)
def ls(kappa,T3_kr,T0):
    return ((kappa)/(kappa-1))*(287.05)*(T3_kr-T0)
def eta_s(liz,ls):
    return (liz)/(ls)
def Ns(mstr,ls):
    return mstr*ls

#obliczenia turbiny

def m_prim(D2D1, phi, beta_2, psi, alpha_2):
    return (1 / math.pow(psi,2)) * ( math.pow( ( math.pow(D2D1,2)*(1 - math.pow(psi,2) * (1-math.pow(math.cos(beta_2 * math.pow(psi,2),2))))) / (math.pow(math.cos(alpha_2),2) + math.pow(D_2D1,2) * (1-math.pow(psi,2))),0.5 ))

def u_str_prim(psi,D2D1, beta_2, m, phi,alpha_2):
    return 1

def rho(n,psi,phi,alpha_2, u_var_1):
    return 1

def m_str_s(m_str, D_s):
    return (m_str + D_s)

def B_s(P_e, eta_c):
    return 1

def B_s(P_e,W,eta_c):
    return 1

def n_s(n_t):
    return n_t

def N_s(N_t):
    return N_t

def pi_3(P_3, P_1):
    return P_3 / P_1



#zapis danych do modelu
def TurboResult(request):
     T0=288.15
     P0=1013287
     rho0=1.225
     c0=0
     param=TurboModel.objects.all().last()
     V=param.objetosc_skokowa
     n1=param.maksymalne_obroty_silnika
     etav=param.wspolczynnik_napelnienia
     kappa=param.kappa
     sprez=param.sprez
     C1a=param.c1a
     etah=param.etah
     a=TurboResultModel(
          strumien_masy_powietrza=m_str(V,n1,rho0,etav),
          praca_izentropowa=l_iz(T0,sprez,kappa),
          temperatura_w_przekroju_wejsciowym=T1(T0,C1a,u2(l_iz(T0,sprez,kappa),etah)),
          predkosc_obwodowa=u2((l_iz(T0,sprez,kappa)),etah),
          predkosc_wzgledna_na_wlocie=1,
          u1=u1(u2(l_iz(T0,sprez,kappa),etah),1),
          P1=1,#p1(0.97,P0,T1(T0,C1a,u2(l_iz(T0,sprez,kappa),etah)),T0,kappa),
          beta1=beta1(C1a,w1(0.9,T1(T0,C1a,u2(l_iz(T0,sprez,kappa),etah)),kappa)),
          mi=mi(131,0.6,0.3),
          c2u=c2u(mi(131,0.6,0.3),u2((l_iz(T0,sprez,kappa)),etah)),
          c2=c2(c2u(mi(131,0.6,0.3),u2((l_iz(T0,sprez,kappa)),etah)) , C1a),
          w2=w2(u2((l_iz(T0,sprez,kappa)),etah) , c2u(mi(131,0.6,0.3),u2((l_iz(T0,sprez,kappa)),etah)) , C1a),
          beta2=1,#beta2(90.00,w2),
          T2=round(1,3),
          p2=1,
          A1=1,
          D2=1,
          D1=1,
          D0=1,
          b=1,
          h1=1,
          rp=1,
          D2_kr=1,
          c2_kr=1,
          T2_kr=1,
          P2_kr=1,
          T3=1,
          p3=1,
          A3=1,
          n=1,
          ls=1,
          eta_s=1,
          Ns=1,
        # m_str_st=1,
          B_st=1,
          rhot=1,
          Wt=1,
          ntt=1,
          Ntt2=1,
          sprezt=1,
          lambda_izt=1,
          tao=1,
          a_kr1t=1,
          c_izt=1,
          u_2t=1,
          u_3t=1,
          c2t=1,
          lambdac2t=1,
          T2t=1,
          P2t=1,
          W2t=1,
          T2_primrt=1,
          P2_primrt=1,
          piwt=1,
          w3t=1,
          Tprim3t=1,
          akr3t=1,
          T2tt=1,
          C3tt=1,
          beta_1t=1,
          D1t=1,
          D2t=1,
          D0t=1,
          h1t=1,
          rp1=1,
          hw1=1,
          zt=1,
          rkwt=1,
          rkzt=1,
          rszkt=1,
          r0t=1,
     )
     a.save()
     rezultaty=TurboResultModel.objects.all().last() 
     return render(request,"TurboResult.html",{'wyniki':rezultaty})


