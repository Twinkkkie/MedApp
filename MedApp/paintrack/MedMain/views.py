from django.shortcuts import render, redirect
from .models import Regiser, Autorization, Info
from .forms import RegiserForm, AutorizationForm, InfoForm
from django.shortcuts import render
from django.views.generic import TemplateView


def registration(request):
    reg = Regiser.objects.all()
    error = ''
    if request.method == "POST":
        form = RegiserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Info')
        else:
            error = 'Error'

    form = RegiserForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'MedMain/Registration.html', context)


def login(request):
    reg_1 = Autorization.objects.all()
    error = ''

    if request.method == "POST":
        form = AutorizationForm(request.POST)
        if form.is_valid():
            data_1 = form.cleaned_data.get("Name_Auto")
            data_2 = form.cleaned_data.get("Password_Auto")
            data_3 = form.cleaned_data.get("Password_confirmation_Auto")
            reg = Regiser.objects.all()
            for i in reg:
                a = i.FIO
                if data_1 == a:
                    if Regiser.objects.filter(FIO=data_1, Password=data_2, Password_confirmation=data_3):
                        b = Regiser.objects.filter(FIO=data_1, Password=data_2, Password_confirmation=data_3)
                        print(b)
                        return redirect('Main')
                    else:
                        print('ERROR')
                        error = 'Error'

    form = AutorizationForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'MedMain/Login.html', context)


def info(request):
    info_1 = Info.objects.all()
    error = ''

    if request.method == "POST":
        form = InfoForm(request.POST)
        reg = Regiser.objects.all()
        if form.is_valid():
            for i in reg:
                a = Regiser.objects.latest('id')
            print(a, a.id)

            data_2 = form.cleaned_data.get("Height")
            data_3 = form.cleaned_data.get("Weight")
            data_4 = form.cleaned_data.get("Diseases")
            form.save()

            for i in info_1:
                b = Info.objects.latest('id')
            print(b, b.id)
            print(a, a.id, b, b.id)

            return redirect('Congratulations')

    form = InfoForm()
    context = {
        'form': form,
    }
    return render(request, 'MedMain/Information.html', context)


def Congrat(request):

    return render(request, 'MedMain/Congratulations.html')


def Main(request):

    return render(request, 'MedMain/MainPage.html')

def intensity(request):

    return render(request, 'MedMain/PainIntensity.html')

class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'