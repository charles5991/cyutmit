from django.shortcuts import render



def sysSettings(request):
    return render(request, 'sysSettings/sysSettings.html')