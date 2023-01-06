from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient-care-home'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('measure/<int:pk>/', views.MeasureDetailView.as_view(), name='measure-detail'),
    path('measure/', views.MeasureListView.as_view(), name='measure-list'),
    path('measure/create/', views.MeasureCreateView.as_view(), name='measure-create'),
    path('measure/<int:pk>/update/', views.MeasureUpdateView.as_view(), name='measure-update'),
    path('unit/create/', views.UnitCreateView.as_view(), name='unit-create'),
    path('unit/', views.UnitListView.as_view(), name='unit-list'),
    path('unit/<int:pk>/', views.UnitDetailView.as_view(), name='unit-detail'),
    path('unit/<int:pk>/update/', views.UnitUpdateView.as_view(), name='unit-update'),
    path('unit/<int:pk>/delete/', views.UnitDeleteView.as_view(), name='unit-delete'),
    path('patient/<int:pk>/measures/', views.PatientMeasureListView.as_view(), name='patient-measure-list'),
]
