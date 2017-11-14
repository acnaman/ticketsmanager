from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Seat

# Create your views here.

def index(request):
    # seat = get_object_or_404(Seat, pk='id')
    return render(request, 'tickets/index.html')#, {'seat': seat})