from django.urls import path
from order.views import index, page1, page2


urlpatterns = [
    path('', index),
    path('page1/', page1),
    path('page2/', page2),
]
