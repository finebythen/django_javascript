from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
import pandas as pd
import json

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


def javascript_sidebar(request):
    return render(request, 'app_django_javascript/view/django_javascript_sidebar.html')


def javascript_table_hide_columns(request):

    list_cols = ['first_name', 'last_name', 'age', 'gender']
    dict_data = {
        'first_name': ['John', 'Jane', 'Michael'],
        'last_name': ['Doe', 'Doe', 'Smith'],
        'age': [33, 32, 51],
        'gender': ['Male', 'Female', 'Male'],
    }

    df_data = pd.DataFrame(dict_data, columns=list_cols)
    json_raw = df_data.to_json(orient='records')
    json_data = json.loads(json_raw)

    context = {'json_data': json_data}
    return render(request, 'app_django_javascript/view/django_javascript_table_hide_columns.html', context)


def javascript_dropdown_create(request):
    form = CarModelOrderForm()
    if request.method == 'POST':
        form = CarModelOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Javascript_Dropdown_Create')
    context = {'formset': form}
    return render(request, 'app_django_javascript/create/django_javascript_dropdown.html', context)


def javascript_dropdown_update(request, pk):
    order = get_object_or_404(DropdownOrder, pk=pk)
    form = CarModelOrderForm(instance=order)
    if request.method == 'POST':
        form = CarModelOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("Javascript_Dropdown_Update", pk)

    context = {'formset': form}
    return render(request, 'app_django_javascript/create/django_javascript_dropdown.html', context)


def javascript_dropdown_load_models(request):
    car_id = request.GET.get('car_id')
    model = DropdownCarModel.objects.filter(car_id=car_id).all()

    context = {'model': model}
    return render(request, 'app_django_javascript/dropdowns/car_model_dropdown_list.html', context)

