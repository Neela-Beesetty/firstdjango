from django.shortcuts import render, redirect
from django.http import Http404

from inventory.models import Item

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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
def accounts(request):
    return render(request, 'inventory/accounts.html')

def about(request):
    return render(request, 'inventory/about.html')

def contact(request):
    return render(request, 'inventory/contact.html')

def buy(request):
    return render(request, 'inventory/buy.html')
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/signup.html', {'form': form})

# Create your views here.
