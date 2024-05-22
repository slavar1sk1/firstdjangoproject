from django import forms


class Post(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "text",
                                                        "placeholder": "Some text here"}), label='', max_length=3000)