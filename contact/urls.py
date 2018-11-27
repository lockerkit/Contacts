from django.urls import path
from . import views

app_name = 'contact'

#Ophalen pagina's 
urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('search', views.contact_search, name='contact_search'),
    path('person/<int:pk>', views.contact_detail, name='contact_detail'),
    path('person/new', views.contact_new, name='contact_new'),
    path('person/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('person/<int:pk>/delete', views.contact_delete, name='contact_delete'),
]
