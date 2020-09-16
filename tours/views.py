from django.views.generic import TemplateView
from django.http import HttpResponseNotFound


class MainView(TemplateView):
    template_name = 'index.html'


class DepartureView(TemplateView):
    template_name = 'departure.html'


class TourView(TemplateView):
    template_name = 'tour.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound('404')


def custom_handler500(request, *args):
    return HttpResponseNotFound('500')
