from django.urls import path
from blog.views import page6, page7, page8


urlpatterns = [
    path('page6/', page6),
    path('page7/', page7),
    path('page8/', page8),
]
