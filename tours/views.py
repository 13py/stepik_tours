from django.http import Http404
from django.shortcuts import render
from django.views import View
from . data import tours, departures


class MainView(View):
    def get(self, request):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure):
        if departure not in departures:
            raise Http404
        return render(request, 'tours/departure.html', context={'departure': departures[departure]})


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404
        return render(request, 'tours/tour.html', context={'tour': tours[id]})


def my_handler404(request, exception=None):
    print(request)
    return render(request, '404.html')


def my_handler500(request, exception=None):
    print(request)
    return render(request, '500.html')
