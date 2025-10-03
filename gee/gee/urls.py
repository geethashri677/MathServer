from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('bodymassindex/',views.bmi,name="bodymassindex"),
    path('',views.bmi,name="bodymassindexroot")
]