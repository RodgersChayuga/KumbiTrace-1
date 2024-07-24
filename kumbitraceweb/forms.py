from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser, MissingPerson, Tip

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-1 text-base font-medium text-[#6B7280] rounded-md bg-transparent',
        'placeholder': 'Username or Email',
        'autofocus': True
    }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-1 text-base font-medium text-[#6B7280] rounded-md bg-transparent',
            'placeholder': 'Password',
            'autocomplete': 'current-password'
        }),
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

class MissingPersonForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

    class Meta:
        model = MissingPerson
        exclude = ['case_number', 'reporter', 'status', 'date_reported', 'last_updated']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'last_seen_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'last_seen_location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'contact_person_type': forms.Select(attrs={'class': 'form-control'}),
            'contact_person_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_contact_person_phone(self):
        phone = self.cleaned_data.get('contact_person_phone')
        if not phone:
            raise forms.ValidationError("Contact person phone number is required.")
        if not phone.startswith('+254') and not phone.startswith('0'):
            raise forms.ValidationError("Phone number must start with '+254' or '0'.")
        if phone.startswith('0') and len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long when starting with '0'.")
        if phone.startswith('+254') and len(phone) != 13:
            raise forms.ValidationError("Phone number must be 13 digits long when starting with '+254'.")
        return phone

class TipForm(forms.ModelForm):
    missing_person = forms.ModelChoiceField(
        queryset=MissingPerson.objects.filter(status='approved'),
        empty_label="Select a case",
        required=True
    )

    class Meta:
        model = Tip
        fields = ['missing_person', 'content', 'phone_number', 'x_username']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your tip here'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'x_username': forms.TextInput(attrs={'placeholder': 'Enter your X username (e.g., @username)'}),
        }

    def __init__(self, *args, **kwargs):
        super(TipForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['x_username'].required = False
        
        # If a missing person is already selected, make the field readonly
        if 'initial' in kwargs and kwargs['initial'].get('missing_person'):
            self.fields['missing_person'].widget.attrs['readonly'] = True