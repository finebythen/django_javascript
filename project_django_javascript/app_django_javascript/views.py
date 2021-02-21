from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

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


def javascript_button_scroll_top(request):
    return render(request, 'app_django_javascript/view/django_javascript_scroll_top_button.html')


def javascript_ajax_create(request):
    form = AjaxCreateForm()
    data = {}

    if request.is_ajax():
        form = AjaxCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    context = {'formset': form}
    return render(request, 'app_django_javascript/create/django_javascript_ajax_create.html', context)
