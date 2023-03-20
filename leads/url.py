from django.urls import path
from .views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView

app_name = 'leads'

urlpatterns = [
   path('all/',LeadListView.as_view(),name='lead-list'),
   path('<int:pk>/',LeadDetailView.as_view(),name='lead-detail'),
   path('<int:pk>/edit/',LeadUpdateView.as_view(),name='lead-edit'),
   path('<int:pk>/delete/',LeadDeleteView.as_view(),name='lead-delete'),
   path('create/',LeadCreateView.as_view(),name='lead-create'),
]