# from django import forms
# from django.contrib.auth.models import User
#
#
# class RegistrationForm(forms.ModelForm):
# 	password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
#
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password']
# 		widgets = {
# 			'password': forms.PasswordInput(),
# 		}
#
# 	# Custom validation for passwords match
# 	def clean(self):
# 		cleaned_data = super().clean()
# 		password = cleaned_data.get("password")
# 		password_confirm = cleaned_data.get("password_confirm")
#
# 		if password and password_confirm and password != password_confirm:
# 			self.add_error('password_confirm', "Passwords do not match")
#
# 		return cleaned_data
#
# 	# Custom validation for username and email uniqueness
# 	def clean_username(self):
# 		username = self.cleaned_data.get('username')
# 		if User.objects.filter(username=username).exists():
# 			raise forms.ValidationError("This username is already taken")
# 		return username
#
# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		if User.objects.filter(email=email).exists():
# 			raise forms.ValidationError("This email is already in use")
# 		return email
