from django.contrib import admin
from django.urls import path,include
from .views import (view_data_detail,size_data,
base,delete_data,upload_data,predict_csv_multi,view_data,analysis,change_password,login2,add_files_multi,detection,dashboard,userLogout,reports,upload_credit_data,prediction_button)
from . import views
#about
urlpatterns = [
    
    
   
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('fraud_detection/',detection,name='detection'),
    path('dashboard/',dashboard,name='dashboard'),
    path('reports/',reports,name='reports'),
    path('upload_credit_data/',upload_credit_data,name='upload_credit_data'),
    path('prediction_button/',prediction_button,name='prediction_button'),
    
    #for main adminstrator upload 
    
    path('upload_data/',upload_data,name='upload_data'),
    path('delete_data/<int:id>/',delete_data,name='delete_data'),


    
    path('add_files_multi/', views.add_files_multi, name='add_files_multi'),


    
    
    path('predict_csv_multi/', views.predict_csv_multi, name='predict_csv_multi'),
    
    
    path('change_password/',change_password,name='change_password'),
    path('analysis/<str:file_name>/', views.analysis, name='analysis'),
    path('size_data/<str:file_name>/', views.size_data, name='size_data'),
    path('view_data/', views.view_table, name='view_data'),
    path('view_data/<str:file_name>/', views.view_data_detail, name='view_data_detail'),
    
    
]


