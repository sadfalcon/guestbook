from django import forms


class CardForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя')
    mail = forms.EmailField(max_length=200, required=True, label='Почта')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)



