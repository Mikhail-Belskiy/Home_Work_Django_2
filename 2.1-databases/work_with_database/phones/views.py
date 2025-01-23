from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    phone_all = Phone.objects.all()
    if sort_param == 'name':
        phone_all = phone_all.order_by('name')
    elif sort_param == 'min_price':
        phone_all = phone_all.order_by('price')
    elif sort_param == 'max_price':
        phone_all = phone_all.order_by('-price')
    context = {'phones': phone_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
