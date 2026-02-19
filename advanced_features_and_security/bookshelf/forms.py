from django import forms

class ExampleForm(forms.Form):
    # Form validation sanitizes input automatically
    book_title = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)