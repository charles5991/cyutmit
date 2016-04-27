from django.contrib import messages
from django.forms.utils import ErrorList
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import boto
from cyutmit.settings import LOGIN_URL, GS_ACCESS_KEY, GS_SECRET_KEY, GS_BUCKET_NAME, GS_URL


def main(request):
    return render(request, 'main/main.html')


def admin_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(LOGIN_URL)
        if request.user.username!='admin':
            messages.error(request, _('沒有權限'))
            return render(request, 'main/main.html')
        return fun(request, *args, **kwargs)
    return auth



def upload(request):    
    if request.method=='POST':
        fileToUpload = request.FILES['fileToUpload']
        folderName = request.POST.get('folderName', '')
        fileName = folderName + '/' + fileToUpload.name
        conn = boto.connect_gs(gs_access_key_id=GS_ACCESS_KEY,
                               gs_secret_access_key=GS_SECRET_KEY)
        bucket = conn.get_bucket(GS_BUCKET_NAME)
        k = boto.gs.key.Key(bucket)
        k.key = fileName
        k.set_contents_from_file(fileToUpload, policy='public-read')
        return HttpResponse(GS_URL + fileName)
    return HttpResponse('upload fail')


customErrors = {
    'required': '必填',
}


class ErrorMessage(ErrorList):
    def __str__(self):
        return ', '.join([e for e in self])
