from django.shortcuts import render


def teachers(request):
    return render(request, 'companys/companys.html')