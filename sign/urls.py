from django.urls import path
from .views import CreateWriter, UpdateWriter


urlpatterns = [
    path('create_writer/', CreateWriter.as_view(), name='create_writer'),
    path('edit_writer/<int:pk>', UpdateWriter.as_view(), name='edit_writer'),
]