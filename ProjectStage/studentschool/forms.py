from django import forms


class StudentSearch(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control text-center',
            'placeholder':"Entre student's name (Ex: KOUHOU MOHAMED)",
            'required':"required",
            'width':'100%'

    }
    ))
