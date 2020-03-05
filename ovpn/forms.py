from django import forms

class TeamForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
        	attrs={
            "class": "form-control",
            "placeholder": "Team Name"
        }),
        required=True
    )
    desc = forms.CharField(
    	widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Team Description"
        }),
        required = True
    )
    blocks = [('0', 'mở'), ('1', 'đóng')]
    block = forms.ChoiceField(
    	widget=forms.Select(
        attrs={
            "class": "form-control",
        }),
        choices=(blocks),
        initial='3', required = True
    )