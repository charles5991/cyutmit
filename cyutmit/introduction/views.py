from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main.views import admin_required
from introduction.forms import IntroductionsForm
from introduction.models import Introduction



def introduction(request):
    return render(request, 'introduction/introduction.html')


def viewIntroduction(request, introductionId):
    context = {'introduction':Introduction.objects.get(id=introductionId)}
    return render(request, 'introduction/viewIntroduction.html', context)


@admin_required
def addIntroduction(request):
    template = 'introduction/addIntroduction.html'
    if request.method=='GET':
        return render(request, template, {'form':IntroductionsForm(), 'folderName':'introduction'})
    # POST
    form = IntroductionsForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    messages.success(request, '消息已發布')
    return redirect('introduction:introduction')


@admin_required
def editIntroduction(request, introductionId):
    template = 'news/editIntroduction.html'
    newsToUpdate = get_object_or_404(Introduction, id=introductionId)
    if request.method=='GET':
        return render(request, template, {'form':IntroductionsForm(instance=newsToUpdate), 'news':newsToUpdate, 'folderName':'news'})
    # POST
    form = IntroductionsForm(request.POST, instance=newsToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'news':newsToUpdate, 'command':'news'})
    form.save()
    messages.success(request, '消息修改成功')
    return redirect('introduction:introduction')
