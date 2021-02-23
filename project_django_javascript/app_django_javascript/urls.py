from django.urls import path
from . import views


urlpatterns = [
    path('javascript/alert/', views.javascript_alert, name="Javascript_Alert"),
    path('javascript/table-filter/', views.javascript_table_filter, name="Javascript_Table_Filter"),
    path('javascript/button-scroll-top/', views.javascript_button_scroll_top, name="Javascript_Button_Scroll_Top"),
    path('javascript/ajax/create/', views.javascript_ajax_create, name="Javascript_Ajax_Create"),
    path('javascript/sidebar/', views.javascript_sidebar, name="Javascript_Sidebar"),
]
