from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import Card
from webapp.forms import CardForm
# Create your views here.

def index_view(request):
    data = Card.objects.all().order_by('-created_at')

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

