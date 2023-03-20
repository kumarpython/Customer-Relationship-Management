from django.forms import ModelForm,widgets
from .models import Agent


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

        labels = {
                    'fname':'First Name',
                    'lname':'Last Name',
                    'dob':'Date of Birth',

                }

        widgets = {
            'dob' : widgets.DateInput(attrs={'type' : 'date'})
        }
