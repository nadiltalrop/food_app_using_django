from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .forms import ItemForm
from .models import Item


def index(request):
    item_list = Item.objects.all()
   
    context = {
        'item_list': item_list,
    }

    return render(request, 'food/index.html', context)


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    
    context = {
        'item': item,
    }

    return render(request, 'food/detail.html', context)


def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context = {
        'form': form,
    }
    
    return render(request, 'food/item-form.html', context)
    

@login_required
def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context = {
        'form': form,
        'item': item,
    }
    
    return render(request, 'food/item-form.html', context)

@login_required
def delete_item(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('food:index')