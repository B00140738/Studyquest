from django import forms
from .models import User
from django.contrib.auth import authenticate

# Sign Up Form

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_pass = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_pass = cleaned_data.get('confirm_pass')

            # Check if passwords match
            if password and confirm_pass and password != confirm_pass:
                self.add_error('confirm_pass', "Passwords do not match")

            return cleaned_data

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password']) # Hash password
            if commit:
                user.save()
            return user

# Login Form

class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    def clean(self):
        cleaned_data = super.clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Authenticate User
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password")
        cleaned_data['user'] = user # Store user login
        return cleaned_data # return data

