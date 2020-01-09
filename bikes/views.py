from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bike
from .forms import BikePostForm
from bikes.models import Bike


def home(request):        
    return render(request, "home/index.html")

def get_bikes(request):
    """
    Create a view that will return a list
    of Bikes that were published prior to 'now'
    and render them to the 'bikeposts.html' template
    by most recent published date
    """
    bikes = Bike.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "bikeposts.html", {'bikes': bikes})
    

def forsale_bikes(request):
    """
    Create a view that will return a list
    of Bikes that were published prior to 'now'
    and render them to the 'bikeposts.html' template
    by most recent published date
    """
    bikes = Bike.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "bikesales.html", {'bikes': bikes})


def bike_detail(request, pk):
    """
    Create a view that returns a single
    Bike object based on the bike ID (pk) and
    render it to the 'bikedetail.html' template.
    Or return a 404 error if the bike is
    not found
    """
    bike = get_object_or_404(Bike, pk=pk)
    bike.views += 1
    bike.save()
    return render(request, "bikedetail.html", {'bike': bike})


def create_or_edit_bike(request, pk=None):
    """
    Create a view that allows us to create
    or edit a bike depending if the Bike ID
    is null or not
    """
    bike = get_object_or_404(Bike, pk=pk) if pk else None
    if request.method == "POST":
        form = BikePostForm(request.POST, request.FILES, instance=bike)
        if form.is_valid():
            bike = form.save()
            return redirect(bike_detail, bike.pk)
    else:
        form = BikePostForm(instance=bike)
    return render(request, 'bikepostform.html', {'form': form})