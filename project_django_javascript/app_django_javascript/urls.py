from django.urls import path
from . import views


urlpatterns = [
    path('javascript/alert/', views.javascript_alert, name="Javascript_Alert"),
    path('javascript/table-filter/', views.javascript_table_filter, name="Javascript_Table_Filter"),
]
