from django.shortcuts import render,redirect
from .models import Products,Category,Tags
from django.http import HttpResponse
from .forms import ProductForm

# Create your views here.
def home(request):
    products=Products.objects.all()
    #tags=products.pop('tags')
    return render(request,'home.html',{'products':products,})

def add(request):
    add=ProductForm()
    if request.method=='POST':
        add=ProductForm(request.POST,request.FILES)
        if add.is_valid():
            add.save()
            return redirect('home')
    else:
        return render(request, 'upload_form.html', {'upload_form':add})
def update_prod(request,prod_id):
    prod_id=int(prod_id)
    try:
        product=Products.objects.get(id=prod_id)
    except Products.DoesNotExist:
        return redirect('home')
    prod_edit=ProductForm(request.POST or None,instance=product)
    if prod_edit.is_valid():
        prod_edit.save()
        return redirect('home')
    return render(request, 'upload_form.html', {'upload_form':prod_edit})

def delete_prod(request,prod_id):
    prod_id=int(prod_id)
    try:
        product=Products.objects.get(id=prod_id)
    except Products.DoesNotExist:
        return redirect('home')
    product.delete()
    return redirect('home')
