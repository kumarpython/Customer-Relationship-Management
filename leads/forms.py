from django.forms import ModelForm,widgets
from leads.models import Lead
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.models import User


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['fname','lname','gender','source','email','dob','city','country']

        labels = {
                    'fname':'First Name',
                    'lname':'Last Name',
                    'dob':'Date of Birth',

                }

        widgets = {
            'dob' : widgets.DateInput(attrs={'type' : 'date'})
        }


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',]
        field_classes = {'username':UsernameField}