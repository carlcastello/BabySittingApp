from django.forms import Form, CharField, EmailField, TextInput
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator, EmailValidator


class UserCreationForm(Form):

    first_name = CharField(
        validators=[
            RegexValidator(regex="^[a-zA-Z]+$", message=None),
            MinLengthValidator(5, message=None),
            MaxLengthValidator(100, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "pattern": "^[a-zA-Z]+$",
                "placeholder": "John",
                "maxlength": 100,
                "data-minlength": 5,
                "data-error": ""
            }
        )
    )

    last_name = CharField(
        validators=[
            RegexValidator(regex="^[a-zA-Z]+$", message=None),
            MinLengthValidator(2, message=None),
            MaxLengthValidator(30, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "pattern": "^[a-zA-Z]+$",
                "placeholder": "Smith",
                "maxlength": 30,
                "data-minlength": 2,
                "data-error": ""
            }
        )
    )

    email = EmailField(
        validators=[
            EmailValidator(message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "john.smith@gmail.com",
                "maxlength": 100,
                "data-minlength": 2,
                "data-error": ""
            }
        )
    )

    contact_number = CharField(
        validators=[
            RegexValidator(regex="^\+?1?\d{9,15}$", message=None),
            MinLengthValidator(10, message=None),
            MaxLengthValidator(100, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "123 456 7890",
                "maxlength": 20,
                "data-minlength": 10,
                "data-error": ""
            }
        )
    )

    address = CharField(
        validators=[
            MinLengthValidator(5, message=None),
            MaxLengthValidator(100, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "123 45th Street",
                "maxlength": 100,
                "data-minlength": 2,
                "data-error": ""
            }
        )
    )

    password = CharField(
        validators=[
            MinLengthValidator(5, message=None),
            MaxLengthValidator(100, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Password",
                "maxlength": 100,
                "data-minlength": 2,
                "data-error": ""
            }
        )
    )

    confirm_password = CharField(
        validators=[
            MinLengthValidator(5, message=None),
            MaxLengthValidator(100, message=None)
        ],
        widget=TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Password",
                "maxlength": 100,
                "data-minlength": 2,
                "data-match": "#id_password",
                "data-error": ""
            }
        )
    )

    class Meta:
        fields = (
            "first_name",
            "last_name",
            "email",
            "contact_number",
            "address",
            "password",
            "confirm_password"
        )
