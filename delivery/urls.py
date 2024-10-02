from django.urls import path
from delivery.views import page3, page4, page5

urlpatterns = [
    path('page3/', page3),
    path('page4/', page4),
    path('page5/', page5),
]
