from django.contrib import admin
from django.urls import path

from apps.email_find.views import update_open_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update-open-email/<int:email_id>/', update_open_email, name='update_open_email')
]
