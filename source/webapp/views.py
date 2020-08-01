from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import Card
#from webapp.forms import CardForm
# Create your views here.

def index_view(request):
    data = Card.objects.all().order_by('-created_at')

    return render(request, 'index.html', context={
        'cards': data
    })
