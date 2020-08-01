from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import Card
from webapp.forms import CardForm
# Create your views here.

def index_view(request):
    data = Card.objects.order_by('-created_at').filter(status='active')

    return render(request, 'index.html', context={
        'cards': data
    })

def card_find(request):
    if request.method == "GET":
        data = Card.objects.filter(name=request.GET.get('name'))
    return render(request, 'index.html', context={
        'cards': data
    })

def card_create_view(request):
    if request.method == "GET":
        return render(request, 'card_create.html', context={
            'form': CardForm()
        })
    elif request.method == 'POST':
        form = CardForm(data=request.POST)
        if form.is_valid():
            card = Card.objects.create(
                name=form.cleaned_data['name'],
                mail=form.cleaned_data['mail'],
                text=form.cleaned_data['text'],
            )
            return redirect('index')
        else:
            return render(request, 'card_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def card_update_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "GET":
        form = CardForm(initial={
            'name': card.name,
            'mail': card.mail,
            'text': card.text,
        })
        return render(request, 'card_update.html', context={
            'form': form,
            'card': card
        })
    elif request.method == 'POST':
        form = CardForm(data=request.POST)
        if form.is_valid():
            # Article.objects.filter(pk=pk).update(**form.cleaned_data)
            card.name = form.cleaned_data['name']
            card.mail = form.cleaned_data['mail']
            card.text = form.cleaned_data['text']
            card.save()
            return redirect('index')
        else:
            return render(request, 'card_update.html', context={
                'card': card,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def card_delete_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'GET':
        return render(request, 'card_delete.html', context={'card': card})
    elif request.method == 'POST':
        card.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])