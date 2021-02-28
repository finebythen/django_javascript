from django.urls import path
from . import views


urlpatterns = [
    path('javascript/alert/', views.javascript_alert, name="Javascript_Alert"),
    path('javascript/table-filter/', views.javascript_table_filter, name="Javascript_Table_Filter"),
    path('javascript/button-scroll-top/', views.javascript_button_scroll_top, name="Javascript_Button_Scroll_Top"),
    path('javascript/ajax/create/', views.javascript_ajax_create, name="Javascript_Ajax_Create"),
    path('javascript/sidebar/', views.javascript_sidebar, name="Javascript_Sidebar"),
    path('javascript/table/hide-columns/', views.javascript_table_hide_columns, name="Javascript_Table_Hide_Columns"),

    # Dependent Dropdowns
    path('javascript/dropdown/add/', views.javascript_dropdown_create, name="Javascript_Dropdown_Create"),
    path('javascript/dropdown/update/<int:pk>/', views.javascript_dropdown_update, name="Javascript_Dropdown_Update"),
    path('ajax/load-models/', views.javascript_dropdown_load_models, name="ajax_load_models"),  # Ajax

]
