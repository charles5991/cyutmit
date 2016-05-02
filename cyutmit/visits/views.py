import boto
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cyutmit.settings import GS_ACCESS_KEY, GS_SECRET_KEY, GS_BUCKET_NAME, \
    GS_URL
from visits.forms import VisitForm
from visits.models import Visit
from main.views import admin_required
from main.views import manager_required


# Create your views here.
def visits(request):
    visits = paginating(request, Visit.objects.all())
    return render(request, 'visits/visits.html', {'visits':visits})


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
    visit = Visit.objects.get(id=visitID)
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


@admin_required
def deleteVisit(request, visitID):
    if request.method=='GET':
        return visits(request)
    # POST
    category = get_object_or_404(Visit, id=visitID)
    category.delete()
    return redirect('visits:visits')

def paginating(request, allVisits):
    paginator = Paginator(allVisits, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        visits = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        visits = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        visits = paginator.page(paginator.num_pages)
    return visits


def searchVisit(request):
    searchTerm = request.GET.get('searchTerm')
    visits = paginating(request, Visit.objects.filter(Q(address__icontains=searchTerm) | Q(suggest__icontains=searchTerm)))
    return render(request, 'visits/visits.html', {'visits':visits})