from django.urls import path
from . import views


urlpatterns = [
    path('routes', views.getRoutes, name='routes'),
    path('mails/<int:pk>', views.mailings, name='info'),
    path('mails/full', views.full_info, name='info-full'),
    path('clients/', views.clients, name='clients'),
    path('messages/', views.messages, name='messages'),
    
    path('create/client', views.createClient, name='create-client'),
    path('delete/client/<int:pk>', views.deleteClient, name='delete-client'),
    path('update/client/<int:pk>', views.updateClient, name='update-client'),
    
    path('create/mailing', views.createMailSender, name='create-mailing'),
    path('delete/mailing/<int:pk>', views.deleteMailing, name='delete-mailing'),
    path('update/mailing/<int:pk>', views.updateMailSender, name='update-mailing'),
]