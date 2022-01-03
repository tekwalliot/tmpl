from django.urls import path
from .import views


urlpatterns = [
    path('', views.main, name='home'),
 
    path('donationsform/<fnc>/<var>/<var1>/', views.donations_form, name='donform'),
    path('donationsform1/<fnc>/<var>/<var1>/', views.donations_form1, name='donform1'),
    path('donations/', views.donations, name='donations'),
    path('expensesform/<fnc>/<var>/', views.expenses_form, name='expnform'),
    path('expenses/', views.expenses, name='expns'),

    path('staffform/<fnc>/<var>/', views.staff_form, name='stfform'),
    path('staff/', views.staff, name='stf'),

    path('catform/<fnc>/<var>/', views.Cat_Form, name='catform'),
    path('donationscategory/', views.Cat, name='cat'),


    path('salariesform/<fnc>/<var>/', views.Salaries_Form, name='salform'),
    path('salaries/', views.salaries, name='sal'),

    path('hundicollectionform/<fnc>/<var>/', views.Hundi_Form, name='hundiform'),
    path('hundicollections/', views.Hundee, name='hnd'),

    path('receipts/<var>/', views.PDF_File, name='receipt'),


    path('chart1/', views.ChartData.as_view()),
    path('upload/<var>', views.upload, name='voiceupload'),
    path('vfn', views.Voice_Name, name='voicename'),
    path('vfg', views.Voice_Gothram, name='voicegothram'),
    # path('userchart1/', views.UserChart.as_view()),
]