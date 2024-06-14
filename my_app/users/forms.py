from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2',
		)

	first_name = forms.CharField()
	last_name = forms.CharField()
	username = forms.CharField()
	email = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()


class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'password',)

	"""
	Переназначение полей. В первом случае просто оставляем пустыми, во втором добавляем всю необоходимую доп инфу:
	плейсхолдеры и тд. Чтобы детально посмотреть как это деалется нажди на cntrl и левой кнобкой по AuthenticationForm
	"""
	# username = forms.CharField()
	# password = forms.CharField()

	# username = forms.CharField(
	# 	label = 'Name',
	# 	widget = forms.TextInput(attrs = {
	# 		'autofocus': True,
	# 		'class': 'form-control',
	# 		'placeholder': 'Enter here your username plz!'
	# 	})
	# )
	# pusername = forms.CharField(
	# 	label = 'Name',
	# 	widget = forms.PasswordInput(attrs = {
	# 		'autocomplete': 'current-password',
	# 		'class': 'form-control',
	# 		'placeholder': 'Enter here your password plz!'
	# 	})
	# )
