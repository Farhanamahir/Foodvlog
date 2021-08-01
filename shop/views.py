from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from . models import *

# Create your views here.
def prodetails(request,c_slug,products_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=products_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pro':prod})

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=product.objects.all().filter(category=c_page,avaliable=True)
    else:
        prodt = product.objects.all().filter(avaliable=True)
    ct=categ.objects.all()
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pr=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pr=paginator.page(paginator.num_pages)
    return render(request,"index.html",{'pro':prodt,'ct':ct,'pg':pr})
def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pro':prod})



