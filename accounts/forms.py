import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

PHONE_RE = re.compile(r'^\+\d{8,15}$')


class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    identifier = forms.CharField(label="Email or phone number")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_identifier(self):
        value = self.cleaned_data['identifier'].strip().replace(' ', '').replace('-', '')
        User = get_user_model()
        if '@' in value:
            validate_email(value)
            if User.objects.filter(email__iexact=value).exists():
                raise ValidationError("An account with this email already exists.")
            return value.lower()
        if not PHONE_RE.match(value):
            raise ValidationError("Enter a phone number with country code, like +919876543210.")
        if User.objects.filter(phone=value).exists():
            raise ValidationError("An account with this phone number already exists.")
        return value

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        cp = cleaned.get('confirm_password')
        if pw and cp and pw != cp:
            self.add_error('confirm_password', "Passwords do not match.")
        elif pw:
            try:
                validate_password(pw)
            except ValidationError as e:
                self.add_error('password', e)
        return cleaned


class LoginForm(forms.Form):
    identifier = forms.CharField(label="Email or phone number")
    password = forms.CharField(widget=forms.PasswordInput)


class OTPForm(forms.Form):
    code = forms.CharField(max_length=6, min_length=6, label="6-digit code")