from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView

from agents.models import Agent
from .models import Lead
from .forms import LeadForm,CustomUserForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(LoginRequiredMixin,CreateView):
    form_class = CustomUserForm
    template_name = 'registration/signup.html'
    success_message = 'New User created successfully'

    def get_success_url(self) :
        return reverse('leads:login')

    def form_valid(self, form) :
        # Send Email
        send_mail(subject='New Lead Created',
                  message='New Lead was created successfully',
                  from_email='test@test.com',
                  recipient_list=['test2@test.com', ])

        return super(LeadCreateView, self).form_valid(form)


class LeadListView(LoginRequiredMixin,ListView):
    model = Lead
    context_object_name = 'leads'
    template_name = 'lead/lead_list.html'


class LeadDetailView(LoginRequiredMixin,DetailView):
    model = Lead
    context_object_name = 'lead'
    template_name = 'lead/lead_detail.html'


class LeadCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = LeadForm
    model = Lead
    template_name = 'lead/lead_create.html'
    success_message = 'New Lead was created successfully'

    def get_success_url(self) :
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # Assign New Leads to Creator-Agent's Company
        Lead.company = Agent.company

        # Status 'New' for new leads
        Lead.status = 'New'

        # Send Email
        send_mail(subject='New Lead Created',
                  message='New Lead was created successfully',
                  from_email='test@test.com',
                  recipient_list=['test2@test.com',])

        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    form_class = LeadForm
    model = Lead
    template_name = 'lead/lead_edit.html'
    success_message = 'Lead was Updated successfully'

    def get_success_url(self) :
        return reverse('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Lead
    template_name = 'lead/lead_delete.html'
    success_message = 'Lead was Deleted successfully'

    def get_success_url(self) :
        return reverse('leads:lead-list')

