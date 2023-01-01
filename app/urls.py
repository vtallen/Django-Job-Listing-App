from django.urls import path

from app.views import hello
from app.views import job_detail


urlpatterns = [
    path('', hello),
    path('job/1', job_detail)
]