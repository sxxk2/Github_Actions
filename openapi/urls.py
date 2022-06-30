from django.urls import path

from .views import OpenAPISewerPipeInfoApiView

app_name = "openapi"

urlpatterns = [
    path('data/save-previous_data/<start_date>/<end_date>/',
         OpenAPISewerPipeInfoApiView.as_view(), name='save_previous_data'),
]