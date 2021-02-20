from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import numpy as np

from .forms import *
from .models import *


def javascript_alert(request):
    # initiate data
    person_name = ""

    # create form
    form = AlertForm()

    if request.method == 'POST' and 'alert-submit' in request.POST:
        form = AlertForm(request.POST, request.FILES)
        if form.is_valid():
            str_first_name = request.POST.get('first_name', None)
            str_last_name = request.POST.get('last_name', None)
            person_name = f"{str_first_name} {str_last_name}"

            form.save()
            return redirect("Javascript_Alert")
        else:
            messages.add_message(request, messages.ERROR, "Fehler: Erstellung 'AlertModel'!")

    context = {'formset': form, 'person_name': person_name}
    return render(request, 'app_django_javascript/create/django_javascript_alert.html', context)


def javascript_table_filter(request):
    # database query
    qs_data = AlertModel.objects.all()

    context = {'qs_data': qs_data}
    return render(request, 'app_django_javascript/view/django_javascript_table_filter.html', context)
