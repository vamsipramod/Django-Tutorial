from django.conf.urls import url
from companies import views

urlpatterns = [
    url(r'^$', views.StockList.as_view())
]
