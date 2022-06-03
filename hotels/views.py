from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from hotels.forms import DateForm

from .models import *

def home(request):
    return render(request, 'hotels/home.html')

def about(request):
    return render(request, 'hotels/about.html')


def contact(request):
    return render(request, 'hotels/contact.html')


def search(request):
    return render(request, 'hotels/search.html')


def index(request):
    hotels_list = Hotel.objects.order_by('id')
    template = loader.get_template('hotels/index.html')

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

    request.session['start_date'] = start_date
    request.session['end_date'] = end_date

    context = {
        'hotels_list': hotels_list,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'hotels/index.html', context)

def detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    start_date = request.session['start_date']
    end_date = request.session['end_date']

    context = {
        'hotel': hotel,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'hotels/detail.html', context)

def displayRoom(request, hotel_id, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request,'hotels/room.html', {'room': room})

def bookRoom(request, hotel_id, room_id):
    room = get_object_or_404(Room, pk=room_id)
