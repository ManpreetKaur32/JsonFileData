from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from myjson import settings

urlpatterns = [
    # path('myfile', views.json_record, name="json data saved in database"),
    path('display', views.json_record, name="display record code"),
    path('show', views.display_data, name="show data"),
    path('', views.home, name="home"),
    # path('category', views.display_data, name="show data"),
    # path('show', views.display_data),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

