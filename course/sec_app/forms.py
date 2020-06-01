from django import forms
from django.core import validators


# custom validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name must be start with 0")


class FormName(forms.Form):
    # for custom validation use this
    # name = forms.CharField(validators=[check_for_z])

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email again:")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()  # to grab of all the fields of the form and it returns dictionary
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email doesn't match")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha bot!")
    #     return botcatcher
