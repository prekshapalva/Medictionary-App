from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url
from . import views
# Django admin customization
admin.site.site_title = "Hospital ABC "
admin.site.site_header = "Hopitalmanagement - Dashboard"
admin.site.index_title = "Hopitalmanagement - Dashboard"

# Paths for each attribute
urlpatterns = [
    path('', views.about, name='about'),
    path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),
    path('administrator', views.administrator, name='administrator'),
    path('doctors', views.doctors, name='doctors'),
    path('patient', views.patient, name='patient'),
    path('patient_p1', views.patient_p1, name='patient_p1'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('payment', views.payment, name='payment'),
    path('patient_appointment', views.patient_appointment, name='patient_appointment'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('tables_patients', views.tables_patients, name='tables_patients'),
    path('main', views.main, name='main'),
    path('tables_doctors', views.tables_doctors, name='tables_doctors')
    #path(‘/<name>/, views.profile, name=‘profile’),

]