from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.views import admin_required
from news.forms import NewsForm
from news.models import News


def news(request):
    newsList = paginating(request, News.objects.all())
    return render(request, 'news/news.html', {'newsList':newsList})


def viewNews(request, newsId):
    context = {'news':News.objects.get(id=newsId)}
    return render(request, 'news/viewNews.html', context)


def paginating(request, allNews):
    paginator = Paginator(allNews, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        newsList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        newsList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        newsList = paginator.page(paginator.num_pages)
    return newsList


def searchNews(request):
    searchTerm = request.GET.get('searchTerm')
    newsList = paginating(request, News.objects.filter(Q(title__icontains=searchTerm) | Q(content__icontains=searchTerm)))
    return render(request, 'news/news.html', {'newsList':newsList})


@admin_required
def addNews(request):
    template = 'news/addNews.html'
    if request.method=='GET':
        return render(request, template, {'form':NewsForm(), 'folderName':'news'})
    # POST
    form = NewsForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    messages.success(request, '最新消息已發布')
    return redirect('news:news')


@admin_required
def editNews(request, newsId):
    template = 'news/editNews.html'
    newsToUpdate = get_object_or_404(News, id=newsId)
    if request.method=='GET':
        return render(request, template, {'form':NewsForm(instance=newsToUpdate), 'news':newsToUpdate, 'folderName':'news'})
    # POST
    form = NewsForm(request.POST, instance=newsToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'news':newsToUpdate, 'command':'news'})
    form.save()
    messages.success(request, '消息修改成功')
    return redirect('news:news')


@admin_required
def deleteNews(request, newsId):
    if request.method=='GET':
        return news(request)
    # POST
    newsToDelete = get_object_or_404(News, id=newsId)
    newsToDelete.delete()
    messages.success(request, '消息已刪除')
    return redirect('news:news')

