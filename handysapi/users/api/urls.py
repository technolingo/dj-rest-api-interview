from django.conf.urls import url
from . import views

app_name = "api"
urlpatterns = [
    url(
        regex=r'^token/$',
        view=views.ObtainAuthToken.as_view(),
        name='obtain_token'
    ),
    url(
        regex=r'^detail/$',
        view=views.UserDetailAPIView.as_view(),
        name='detail'
    ),
]
