from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def index(request):
    items = Item.objects.exclude(quantity=0)
    return render(request, 'inventory/index.html', {
        'items': items,
        })
def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request,'inventory/item_detail.html',{
        'item': item,
        })

def about(request):
    items = Item.objects.exclude(quantity=0)
    return render(request, 'inventory/about.html', {
        'items': items,
        })
def contact(request):
    items = Item.objects.exclude(quantity=0)
    return render(request, 'inventory/contact.html', {
        'items': items,
        })

# Create your views here.
