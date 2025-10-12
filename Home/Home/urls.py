from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("school.urls")),
    path('student/',include("student.urls")),
    path('authentication/',include("home_auth.urls"))

]
