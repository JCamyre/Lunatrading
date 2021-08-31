from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StatSerializer
from .models import Stat
import os
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


class StatsView(viewsets.ModelViewSet):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()


class Assets(View):

    def get(self, _request, filename):  # Handling when a HttpResponse is sent to user
        # The views.py in your React frontend needs a content_type argument in the HttpResponse.
        # Heroku needs to know where the static files are.

        # The "refused to execute script ... MIME type ('text/html')" problem stems from Django's default content_type setting for an HttpResponse, which is text/html.

        # This can be fixed by including a content_type='application/javascript' argument in the return statement of a new class-based view called Assets(View) inside views.py like so:
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()
