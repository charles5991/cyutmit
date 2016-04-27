import boto
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from cyutmit.settings import GS_ACCESS_KEY, GS_SECRET_KEY, GS_BUCKET_NAME, \
    GS_URL
from visits.forms import VisitForm
from visits.models import DemandCategory, Department, Teacher, VisitModel


# Create your views here.
def visits(request):
    return render(request, 'visits/visits.html', {'visits':VisitModel.objects.all()})


def create(request):

    if request.method=='GET':
        return render(request, 'visits/createVisits.html', {'visitForm':VisitForm()})
    
    #POST
    visitsForm = VisitForm(data=request.POST)
    if not visitsForm.is_valid():
        return render(request, 'visits/createVisits.html', {'visitForm':visitsForm})
    
    visitsForm.save()
    
    return redirect(reverse('visits:visits'))


def getVisit(request, visitID):
    visit = VisitModel.objects.get(id=visitID)
    visit = VisitForm(instance=visit)
    return render(request, 'visits/visit.html', {'visitForm':visit})


def upload(request):
    if request.method=='GET':
        fileUrl = request.session.get('fileUrl', '')
        publicRead = request.session.get('publicRead', '')
        if not fileUrl:
            return render(request, 'visits/upload.html')
        #have
        if publicRead:
            return render(request, 'visits/upload.html', {'fileUrl':GS_URL+fileUrl})
        # not publicRead
        conn = boto.connect_gs(gs_access_key_id=GS_ACCESS_KEY,
                               gs_secret_access_key=GS_SECRET_KEY)
        bucket = conn.get_bucket(GS_BUCKET_NAME)
        fpic = boto.gs.key.Key(bucket)
        fpic.key = fileUrl
        fileUrl = fpic.generate_url(expires_in=86400)
        return render(request, 'visits/upload.html', {'fileUrl':fileUrl})
    #post
    uploadFile = request.FILES.get('uploadFile', '')
    publicRead = request.POST.get('publicRead', False)
    conn = boto.connect_gs(gs_access_key_id=GS_ACCESS_KEY,
                           gs_secret_access_key=GS_SECRET_KEY)
    bucket = conn.get_bucket(GS_BUCKET_NAME)
    fpic = boto.gs.key.Key(bucket)  
    fpic.key = 'test/'+uploadFile.name
    if publicRead:
        fpic.set_contents_from_file(uploadFile, policy='public-read')
    request.session['fileUrl'] = fpic.key
    request.session['publicRead'] = publicRead
    return redirect(reverse('visits:upload'))