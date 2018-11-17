from django.conf.urls import url
from . import views

app_name = "permissions"
urlpatterns = [
    url(
        regex=r'^list$',
        view=views.DummyListAPIView.as_view(),
        name='list'
    ),
    url(
        regex=r'^view$',
        view=views.DummyViewAPIView.as_view(),
        name='view'
    ),
    url(
        regex=r'^edit$',
        view=views.DummyEditAPIView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^delete$',
        view=views.DummyDeleteAPIView.as_view(),
        name='delete'
    ),
]
