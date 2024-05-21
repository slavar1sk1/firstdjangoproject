from django import forms


class Post(forms.Form):
    text = forms.CharField(label="text", max_length=3000, widget=forms.TextInput(attrs={'placeholder': 'Some text'}))