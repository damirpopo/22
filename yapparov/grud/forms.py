from django import forms

class userreg(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"pol","placeholder":"name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"pol","placeholder":"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"pol","placeholder":"password"}))


