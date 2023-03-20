from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from agents.forms import AgentForm
from agents.models import Agent


class AgentListView(LoginRequiredMixin,ListView):
    model = Agent
    context_object_name = 'agents'
    template_name = 'agents/agents_list.html'


class AgentDetailView(LoginRequiredMixin,DetailView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'agents/agent_detail.html'


class AgentCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = AgentForm
    model = Agent
    template_name = 'agents/agent_create.html'
    success_message = 'New Agent was created successfully'

    def get_success_url(self) :
        return reverse('agents:agent-list')


class AgentUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    form_class = AgentForm
    model = Agent
    template_name = 'agents/agent_edit.html'
    success_message = 'Agent was Updated successfully'

    def get_success_url(self) :
        return reverse('agents:agent-list')


class AgentDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Agent
    template_name = 'agents/agent_delete.html'
    success_message = 'Agent was Deleted successfully'

    def get_success_url(self) :
        return reverse('agents:agent-list')

# Create your views here.
