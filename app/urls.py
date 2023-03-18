from django.urls import path
from . import views
urlpatterns = [
    path('', views.appIndex, name='app_index'),
    path('<slug:slug>/', views.AppShow, name='app_show'),
    path('contact', views.ContactView.as_view(), name='contact'),
]
# ssss