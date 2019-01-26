from django.conf.urls import url
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    SearchView
)
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('about/', views.about, name='about'),
    url('plan_relocation/', views.PlanRelocation.as_view(), name='plan_relocation'),
    url('contact/', views.contact, name='contact'),
    url('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    url('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    url('subscribe/', views.subscribe, name='subscribe'),
    url('expat_blog/', PostListView.as_view(), name='expat_blog'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    url('results/', SearchView.as_view(), name='search'),
    url('error_page/', views.error_page, name='error_page'),
    url('citizenship/', views.Citizenship.as_view(), name='citizenship'),
    url('success/', views.successView, name='success'),
]

