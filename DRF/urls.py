from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # here studentinfo is the name that shows in the url
    path('studentinfo/<int:pk>', views.Student_detail),
    # to show the student info through the primary key
    path('studentinfo/', views.Student_list),
]
