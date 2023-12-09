from django.urls import path
from firstsite.views import *

app_name="firstsite"

urlpatterns = [
    path('',index_view, name='index'),
]
