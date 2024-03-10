
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('deletedata/<int:id>',views.delete_data,name='delete'),
    path('updatedata/<int:id>',views.update_data,name='update'),
]