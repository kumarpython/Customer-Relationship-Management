from django.urls import path
from .views import AgentCreateView, AgentDeleteView, AgentListView, AgentDetailView, AgentUpdateView

app_name = 'agents'

urlpatterns = [
   path('all/',AgentListView.as_view(),name='agent-list'),
   path('<int:pk>/',AgentDetailView.as_view(),name='agent-detail'),
   path('<int:pk>/edit/',AgentUpdateView.as_view(),name='agent-edit'),
   path('<int:pk>/delete/',AgentDeleteView.as_view(),name='agent-delete'),
   path('create/',AgentCreateView.as_view(),name='agent-create'),
]