from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path('',views.home,name='home'),
    path('test/',views.test,name='test'),
    path('test_doctor/', views.test1, name='test1'),
    path('signup/',views.signup,name='signup'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('login/', views.log, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/', views.forgot_password, name='forgot'),
    path('details/', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('change_password/', views.change_password, name='change_password'),

]