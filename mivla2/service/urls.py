from django.urls import path
from .views import *

app_name = 'service'

urlpatterns = [

    path('', shop, name='catalog'),
    path('api/v1/sofalist', SofaAPIView.as_view()),
    path('api/v1/wardrobelist', WardrobeAPIView.as_view()),
    path('api/v1/stollist', StolAPIView.as_view()),
    path('api/v1/furniturelist', FurnitureAPIView.as_view()),
    path('api/v1/sofalist/<int:pk>', SofaEntityView.as_view()),
    path('api/v1/stollist/<int:pk>', StolEntityView.as_view()),
    path('api/v1/wardrobelist/<int:pk>', WardrobeEntityView.as_view()),
    path('api/v1/furniturelist/<int:pk>', FurnitureEntityView.as_view()),
]
