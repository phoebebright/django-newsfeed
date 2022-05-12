from django import forms


class SubscriberEmailForm(forms.Form):
    email_address = forms.EmailField()
    interest_scoring = forms.BooleanField(initial=False, required=False)
    interest_organising = forms.BooleanField(initial=False, required=False)
