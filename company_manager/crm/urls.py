from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('company/create', views.CompanyCreateView.as_view(), name='company_create'),
    path('company/list', views.CompanyListView.as_view(), name='company_list'),
    path('opportunity/list', views.OpportunityListView.as_view(), name='opportunity_list'),
    path('opportunity/create', views.OpportunityCreateView.as_view(), name='opportunity_create'),
]