from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User()
		fields = ['username', 'password']

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
