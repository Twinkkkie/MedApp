from .models import Regiser, Autorization, Info
from django.forms import ModelForm, TextInput, Textarea


class RegiserForm(ModelForm):
    class Meta:
        model = Regiser
        fields = [
            "FIO",
            "User_name",
            "Email",
            "Phone_number",
            "Password",
            "Password_confirmation",
            "Gender",
            'Gender_1'
        ]
        widgets = {
            "FIO": TextInput(attrs={
                'placeholder': "Введите фамилию, имя, отчество",
                'class': "input-box",
                'id': 'Name',
                'type': "text"
            }),
            "User_name": TextInput(attrs={
                'class': "input-box",
                'id': 'Nickname',
                'type': "text",
                'placeholder': "Введите имя пользователя"
            }),
            "Email": TextInput(attrs={
                'class': "input-box",
                'id': 'Email',
                'type': "text",
                'placeholder': "Введите ваш Email"
            }),
            "Phone_number": TextInput(attrs={
                'class': "input-box",
                'id': 'Number',
                'type': "text",
                'placeholder': "Введите ваш номер телефона"
            }),
            "Password": TextInput(attrs={
                'class': "input-box",
                'id': 'Password',
                'type': "text",
                'placeholder': "Введите ваш пароль"
            }),
            "Password_confirmation": TextInput(attrs={
                'class': "input-box",
                'id': 'Password_2',
                'type': "text",
                'placeholder': "Подтвердите ваш пароль"
            }),
            "Gender": TextInput(attrs={
                'class': "gender-details",
                'id': "dot-1",
                'type': "radio",
            }),
            "Gender_1": TextInput(attrs={
                'class': "gender-details",
                'id': "dot-2",
                'type': "radio",
            }),
        }


class AutorizationForm(ModelForm):
    class Meta:
        model = Autorization
        fields = [
            "Name_Auto",
            "Password_Auto",
            "Password_confirmation_Auto"
        ]
        widgets = {
            "Name_Auto": TextInput(attrs={
                'placeholder': "Введите имя пользователя",
                'class': "input-box",
                'id': 'Nick',
                'type': "text"
            }),
            "Password_Auto": TextInput(attrs={
                'class': "input-box",
                'id': 'Pass_auto',
                'type': "text",
                'placeholder': "Введите ваш пароль"
            }),
            "Password_confirmation_Auto": TextInput(attrs={
                'class': "input-box",
                'id': 'Pass_auto_2',
                'type': "text",
                'placeholder': "Подтвердите ваш пароль"
            }),
        }


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = [
            "Height",
            "Weight",
            "Diseases"
        ]
        widgets = {
            "Height": TextInput(attrs={
                'placeholder': "Введите свой рост",
                'class': "input-box",
                'id': 'height',
                'type': "text"
            }),
            "Weight": TextInput(attrs={
                'class': "input-box",
                'id': 'weight',
                'type': "text",
                'placeholder': "Введите свой вес"
            }),
            "Diseases": Textarea(attrs={
                'class': "input-box-diseases",
                'id': 'diseases',
                'type': "textarea",
                'placeholder': "Введите заболевания"
            }),
        }