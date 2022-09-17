##urls.pyはデフォルトでは作成されていないので作成すること。
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]