from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('applicant-list/',views.applicantList,name="applicant-list"),
   
    path('applicant-list/<str:pk>/',views.applicantDetail,name='applicant-detail'),
    path('applicant-create/',views.applicantCreate,name="applicant-create"),
    path('applicant-update/<str:pk>/',views.applicantUpdate,name="applicant-update"),
    path('applicant-delete/<str:pk>/',views.applicantDelete,name="applicant-delete"),
    
]
