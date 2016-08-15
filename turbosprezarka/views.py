from django.shortcuts import render
from .models import TurboModel
from .forms import TurboForm
from django.shortcuts import render_to_response
from django.shortcuts import redirect

def TurboParametry(request):
     if request.method == 'POST':
        form=TurboForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect(TurboResult)
     else:
        form=TurboForm()
     return render(request,'TurboParametry.html',{'form':form})

def TurboResult(request):
     return render_to_response("TurboResult.html")


# Create your views here.
