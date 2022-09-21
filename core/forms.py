from django import forms

# from django.contrib.auth import password_validation
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Student, MyUser


# class MyUserForm(forms.ModelForm):
#     class Meta:
#         model = MyUser


# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs["class"] = "form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"

#     username = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Enter Username or Email"})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"})
#     )

#     class Meta:
#         model = MyUser


# class UserRegisterForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserRegisterForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs["class"] = "block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"

#     username = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Enter Username"})
#     )
#     password1 = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "new-password", "placeholder": "Enter Password"}
#         ),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=("Password confirmation"),
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "new-password", "placeholder": "Confirm Password"}
#         ),
#         strip=False,
#         help_text=("Enter the same password as before, for verification."),
#     )
#     email = forms.EmailField(
#         widget=forms.TextInput(attrs={"placeholder": "Enter E - Mail"})
#     )

#     class Meta:
#         model = MyUser
#         fields = ("username", "email")

# class GetStudentData(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(GetStudentData, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs["class"] = "block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"

#     search_roll = forms.CharField(widget=forms.TextInput(attrs={"placegolder": "Enter roll to search"}))
